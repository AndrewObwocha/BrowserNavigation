# Browser Navigation

A simple web browser navigation implementation with history tracking functionality.

## Description

This project demonstrates browser-like navigation features including forward and backward movement through visited pages, along with history tracking and management.

## Features

- Basic browser navigation controls (back, forward)
- URL history tracking
- Current page management
- Navigation state handling

## Installation

1. git clone https://github.com/AndrewObwocha/BrowserNavigation.git
2. cd BrowserNavigation

## Usage

Import the navigation module into your project:

## Usage

Import the navigation module into your project:

```python
from browser_navigation import BrowserNavigation

# Create a new browser instance
browser = BrowserNavigation()

# Navigate to pages
browser.navigate_to("https://example.com")
browser.navigate_to("https://example.com/about")

# Go back
previous_page = browser.go_back()

# Go forward
next_page = browser.go_forward()

# View history
history = browser.get_history()
```

## Requirements

Python 3.x

## License

MIT License

## Author

Andrew Obwocha
