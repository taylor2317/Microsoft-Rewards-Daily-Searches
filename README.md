# Automated Browser Search Script

## Overview
This Python script automates browser searches by typing a predefined list of words into the address/search bar at timed intervals using `pyautogui`. It is designed to automate 'Microsoft Rewards' daily searches.

## Requirements
- Python 3.7 or higher
- `pyautogui` library

Install dependency:
```bash
pip install pyautogui
```

## How It Works
- Waits 5 seconds before starting (to allow user to switch to a browser window)
- Focuses the browser address bar using `Ctrl + L`
- Types each word from a predefined list
- Presses Enter to trigger a search
- Waits a configurable interval before repeating
- Stops after the time limit or when the word list ends

## Setup Instructions
1. Copy the script into a `.py` file (e.g., `search_bot.py`)
2. Install dependencies using pip
3. Open your browser (Chrome, Edge, etc.)
4. Run the script:
```bash
python search_bot.py
```
5. Switch to the browser within 5 seconds

## Configuration
You can modify:
- `words` → list of search terms
- `search_interval` → delay between searches (seconds)
- `run_duration` → total runtime (seconds)

## Safety Notes
- Do not use your keyboard or mouse while the script is running
- Ensure the browser window remains focused
- Stop the script immediately if unintended behavior occurs (Ctrl + C in terminal)

## Notes
This script is intended for automation testing and input simulation in a controlled environment.
```
