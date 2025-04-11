# Web Browser Navigation Simulator

## Overview

This Python project simulates the basic back and forward navigation functionality of a web browser using a command-line interface (CLI). It serves as a practical demonstration of how the Stack Abstract Data Type (ADT) can be used to manage browsing history.

The core logic utilizes two stacks: one to keep track of the "back" history and one for the "forward" history. The project includes a simple, self-contained `Stack` class implementation.

## Features

*   Simulates visiting new URLs.
*   Implements "Back" navigation (`<`) to previously visited sites.
*   Implements "Forward" navigation (`>`) to sites visited after going back.
*   Displays the currently viewed (simulated) URL.
*   Uses a simple command-line interface for interaction.
*   Includes a basic `Stack` class implementation (`stack.py`).

## How it Works

The navigation logic relies on two stacks, `back` and `forward`:

1.  **Visiting a New Site (`=`):**
    *   The *current* site is pushed onto the `back` stack.
    *   The `forward` stack is cleared (since going to a new site invalidates the old forward path).
    *   The new site becomes the *current* site.
2.  **Going Back (`<`):**
    *   If the `back` stack is not empty:
        *   The *current* site is pushed onto the `forward` stack.
        *   The top site is popped from the `back` stack and becomes the new *current* site.
    *   If the `back` stack is empty, navigation fails.
3.  **Going Forward (`>`):**
    *   If the `forward` stack is not empty:
        *   The *current* site is pushed onto the `back` stack.
        *   The top site is popped from the `forward` stack and becomes the new *current* site.
    *   If the `forward` stack is empty, navigation fails.

## Requirements

*   Python 3.x
*   The `stack.py` file must be in the same directory as `web_browser.py`.

## Usage

1.  **Ensure files are together:** Place `web_browser.py` and `stack.py` in the same directory.
2.  **Navigate:** Open your terminal or command prompt and navigate to that directory.
3.  **Run the script:**
    ```bash
    python web_browser.py
    # or python3 web_browser.py
    ```
4.  **Interact:** Follow the on-screen prompts:
    *   Enter `=` to simulate visiting a new URL (you'll be prompted for the URL).
    *   Enter `<` to go back in history.
    *   Enter `>` to go forward in history.
    *   Enter `q` to quit the simulator.

## File Structure

*   `web_browser.py`: Contains the main simulation logic, user interaction, and history management using the stacks.
*   `stack.py`: Provides the implementation of the Stack Abstract Data Type used by `web_browser.py`.

## Educational Note

This project primarily demonstrates a common application of the Stack data structure and basic CLI programming concepts. It does **not** actually connect to the internet or render web pages.

## License

MIT License

## Author

Andrew Obwocha
