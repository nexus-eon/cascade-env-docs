"""Automated screenshot generator for documentation.

Uses Playwright to capture consistent screenshots of documentation examples.
Provides configurable options for viewport size, retries, and custom actions.
"""

import asyncio
import json
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from playwright.async_api import Browser, Page, async_playwright  # type: ignore

# Set up logging with debug level
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Constants
DEFAULT_TIMEOUT = 10000  # 10 seconds in milliseconds
MAX_CONNECTION_RETRIES = 3
CONNECTION_RETRY_DELAY = 2  # seconds


class ScreenshotGenerator:
    """Generates screenshots for documentation using Playwright."""

    def __init__(self, config_path: str) -> None:
        """Initialize the screenshot generator.

        Args:
            config_path: Path to the JSON configuration file
        """
        self.config_path = config_path
        self.config = self._load_config()
        self.output_dir = Path(
            self.config.get("output_directory", "docs/assets/screenshots")
        )
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.retries = self.config.get("retries", 3)
        self.retry_delay = self.config.get("retry_delay", 1)
        logging.debug(f"Initialized with config from {config_path}")
        logging.debug(f"Output directory: {self.output_dir}")

    def _load_config(self) -> Dict[str, Any]:
        """Load screenshot configuration from JSON file.

        Returns:
            Dict containing screenshot configuration
        """
        with open(self.config_path) as f:
            config: Dict[str, Any] = json.load(f)
            return config

    async def _setup_page(self, browser: Browser) -> Page:
        """Set up a new page with custom viewport and other settings.

        Args:
            browser: Playwright browser instance

        Returns:
            Configured page object
        """
        logging.debug("Setting up new browser page")
        context = await browser.new_context(
            viewport={
                "width": self.config.get("viewport_width", 1280),
                "height": self.config.get("viewport_height", 720),
            },
            device_scale_factor=self.config.get("device_scale_factor", 1),
        )
        page = await context.new_page()
        page.set_default_timeout(DEFAULT_TIMEOUT)
        page.set_default_navigation_timeout(DEFAULT_TIMEOUT)
        logging.debug(f"Page configured with timeout: {DEFAULT_TIMEOUT}ms")

        # Apply custom CSS if specified
        if "custom_css" in self.config:
            await page.add_style_tag(content=self.config["custom_css"])
            logging.debug("Applied custom CSS")

        return page

    async def _wait_for_network_idle(
        self, page: Page, timeout: int = DEFAULT_TIMEOUT
    ) -> bool:
        """Wait for network to become idle with timeout.

        Args:
            page: Playwright page object
            timeout: Timeout in milliseconds

        Returns:
            bool: True if network became idle, False if timeout occurred
        """
        try:
            logging.debug(f"Waiting for network idle (timeout: {timeout}ms)")
            await page.wait_for_load_state("networkidle", timeout=timeout)
            logging.debug("Network reached idle state")
            return True
        except Exception as e:
            logging.debug(f"Network idle timeout: {str(e)}")
            return False

    async def _handle_dynamic_content(
        self, page: Page, screenshot: Dict[str, Any]
    ) -> None:
        """Handle dynamic content loading and custom actions.

        Args:
            page: Playwright page object
            screenshot: Screenshot configuration dictionary
        """
        if "wait_for_selector" in screenshot:
            selector = screenshot["wait_for_selector"]
            try:
                logging.debug(f"Waiting for selector: {selector}")
                await page.wait_for_selector(selector, timeout=DEFAULT_TIMEOUT)
                logging.debug(f"Found selector: {selector}")
            except Exception as e:
                logging.warning(f"Selector wait timeout: {str(e)}")

        if "before_screenshot" in screenshot:
            for action in screenshot["before_screenshot"]:
                try:
                    if action["type"] == "click":
                        logging.debug(f"Clicking element: {action['selector']}")
                        await page.click(action["selector"], timeout=DEFAULT_TIMEOUT)
                    elif action["type"] == "type":
                        logging.debug(f"Typing into element: {action['selector']}")
                        await page.type(action["selector"], action["text"])
                    await asyncio.sleep(0.5)
                except Exception as e:
                    logging.warning(f"Action failed: {action['type']} - {str(e)}")

    async def _take_screenshot(
        self, page: Page, screenshot: Dict[str, Any], path: Path
    ) -> Tuple[bool, Optional[str]]:
        """Take the actual screenshot.

        Args:
            page: Playwright page object
            screenshot: Screenshot configuration dictionary
            path: Path to save the screenshot

        Returns:
            Tuple of (success: bool, error_message: Optional[str])
        """
        try:
            selector = screenshot.get("selector")
            if selector:
                logging.debug(f"Taking element screenshot: {selector}")
                element = await page.wait_for_selector(
                    selector, timeout=DEFAULT_TIMEOUT
                )
                if element is None:
                    return False, f"Element not found: {selector}"
                await element.screenshot(
                    path=str(path),
                    animations=(
                        "disabled"
                        if screenshot.get("disable_animations", False)
                        else "allow"
                    ),
                )
            else:
                logging.debug("Taking full page screenshot")
                await page.screenshot(
                    path=str(path),
                    full_page=screenshot.get("full_page", False),
                    animations=(
                        "disabled"
                        if screenshot.get("disable_animations", False)
                        else "allow"
                    ),
                    timeout=DEFAULT_TIMEOUT,
                )
            logging.debug(f"Screenshot saved to: {path}")
            return True, None
        except Exception as e:
            error_msg = str(e)
            logging.error(f"Screenshot capture failed: {error_msg}")
            return False, error_msg

    async def _verify_page_loaded(self, page: Page, url: str) -> bool:
        """Verify that the page has loaded successfully.

        Args:
            page: Playwright page object
            url: URL to verify

        Returns:
            bool: True if page loaded successfully
        """
        try:
            logging.debug(f"Navigating to: {url}")
            response = await page.goto(url, wait_until="load", timeout=DEFAULT_TIMEOUT)
            if response is None or not response.ok:
                logging.error(f"Failed to load page: {url}")
                if response:
                    logging.error(f"Status: {response.status}")
                    logging.error(f"Status text: {response.status_text}")
                return False

            logging.debug("Page load complete")
            return True

        except Exception as e:
            logging.error(f"Page load error: {str(e)}")
            return False

    async def _capture_with_retry(self, page: Page, screenshot: Dict[str, Any]) -> bool:
        """Attempt to capture a screenshot with retries.

        Args:
            page: Playwright page object
            screenshot: Screenshot configuration dictionary

        Returns:
            bool: True if screenshot was captured successfully
        """
        name = screenshot["name"]
        url = screenshot["url"]

        for attempt in range(self.retries):
            try:
                logging.info(
                    f"Capturing screenshot: {name} (attempt {attempt + 1}/{self.retries})"
                )

                # Verify page loads correctly
                if not await self._verify_page_loaded(page, url):
                    raise Exception("Page failed to load properly")

                # Allow time for content to settle
                wait_time = screenshot.get(
                    "wait_time", 2
                )  # Default to 2 seconds if not specified
                logging.debug(f"Waiting {wait_time} seconds for content to settle")
                await asyncio.sleep(wait_time)

                # Handle dynamic content
                await self._handle_dynamic_content(page, screenshot)

                # Take screenshot
                screenshot_path = self.output_dir / f"{name}.png"
                success, error = await self._take_screenshot(
                    page, screenshot, screenshot_path
                )

                if success:
                    logging.info(f"Successfully captured: {name}")
                    return True
                else:
                    raise Exception(error)

            except Exception as e:
                logging.error(f"Error capturing {name}: {str(e)}")
                if attempt < self.retries - 1:
                    logging.info(f"Retrying in {self.retry_delay} seconds...")
                    await asyncio.sleep(self.retry_delay)
                else:
                    logging.error(
                        f"Failed to capture {name} after {self.retries} attempts"
                    )
                    return False

        return False

    async def capture_screenshots(self) -> None:
        """Capture all screenshots defined in config."""
        logging.info("Starting screenshot capture process")
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await self._setup_page(browser)

            results: List[Dict[str, Any]] = []
            for screenshot in self.config["screenshots"]:
                success = await self._capture_with_retry(page, screenshot)
                results.append({"name": screenshot["name"], "success": success})

            await browser.close()

            # Report results
            successful = sum(1 for r in results if r["success"])
            total = len(results)
            logging.info(
                f"Screenshot generation complete: {successful}/{total} successful"
            )

            if successful < total:
                logging.warning("Failed screenshots:")
                for result in results:
                    if not result["success"]:
                        logging.warning(f"- {result['name']}")


async def main() -> None:
    """Run the screenshot generator."""
    generator = ScreenshotGenerator("tools/screenshot_config.json")
    await generator.capture_screenshots()


if __name__ == "__main__":
    asyncio.run(main())
