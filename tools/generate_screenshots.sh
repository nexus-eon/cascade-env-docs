#!/bin/bash

# Install dependencies if needed
pip install -r tools/requirements-screenshots.txt

# Install playwright browsers
playwright install chromium

# Run the screenshot generator
python tools/screenshot_generator.py
