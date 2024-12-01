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

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


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
        context = await browser.new_context(
            viewport={
                "width": self.config.get("viewport_width", 1280),
                "height": self.config.get("viewport_height", 720),
            },
            device_scale_factor=self.config.get("device_scale_factor", 1),
        )
        page = await context.new_page()

        # Apply custom CSS if specified
        if "custom_css" in self.config:
            await page.add_style_tag(content=self.config["custom_css"])

        return page

    async def _handle_dynamic_content(
        self, page: Page, screenshot: Dict[str, Any]
    ) -> None:
        """Handle dynamic content loading and custom actions.

        Args:
            page: Playwright page object
            screenshot: Screenshot configuration dictionary
        """
        if "wait_for_selector" in screenshot:
            await page.wait_for_selector(screenshot["wait_for_selector"])

        if "before_screenshot" in screenshot:
            for action in screenshot["before_screenshot"]:
                if action["type"] == "click":
                    await page.click(action["selector"])
                elif action["type"] == "type":
                    await page.type(action["selector"], action["text"])
                await asyncio.sleep(0.5)

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
                element = await page.wait_for_selector(selector)
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
                await page.screenshot(
                    path=str(path),
                    full_page=screenshot.get("full_page", False),
                    animations=(
                        "disabled"
                        if screenshot.get("disable_animations", False)
                        else "allow"
                    ),
                )
            return True, None
        except Exception as e:
            return False, str(e)

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

                # Navigate and wait for content
                await page.goto(url)
                await page.wait_for_load_state("networkidle")
                if "wait_time" in screenshot:
                    await asyncio.sleep(screenshot["wait_time"])

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

        return False  # Return False if all retries failed

    async def capture_screenshots(self) -> None:
        """Capture all screenshots defined in config."""
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
