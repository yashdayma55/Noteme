# NOTE_ME

A feature-rich text editor built with Python Tkinter. Simple, lightweight, and easy to use.

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)

## Features

- **File Operations**
  - New, Open, Save, Save As
  - Exit with unsaved changes prompt
  - Supports `.txt` files with UTF-8 encoding

- **Edit**
  - Copy, Paste, Cut
  - Clear All
  - Find & Replace

- **Formatting**
  - Font selection (all system fonts)
  - Font size (4–200)
  - Bold, Italic, Underline
  - Font color picker
  - Text alignment (Left, Center, Right)

- **View**
  - Toggle Toolbar
  - Toggle Status Bar

- **Color Themes**
  - Light Default
  - Light Pulse
  - Dark Pulse
  - Red Pulse
  - Blue Pulse
  - Yellow Pulse

## Requirements

- Python 3.7 or higher
- Tkinter (included with most Python installations)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yashdayma55/Noteme.git
   cd note_me
   ```

2. Run the application:
   ```bash
   python note_me.py
   ```

## Usage

| Action        | Shortcut      |
|---------------|---------------|
| New File      | `Ctrl + N`    |
| Open File     | `Ctrl + O`    |
| Save          | `Ctrl + S`    |
| Save As       | `Ctrl + Alt + S` |
| Exit          | `Ctrl + D`    |
| Find & Replace| `Ctrl + F`    |
| Clear All     | `Ctrl + Alt + X` |

## Project Structure

```
note_me/
├── note_me.py          # Main application
├── setup.py            # Build script for cx_Freeze (Windows executable)
├── atomwriter icon/    # Icon assets for the UI
├── icon.ico            # Application icon
└── README.md
```

## Building an Executable (Optional)

To create a standalone Windows executable using cx_Freeze:

1. Install cx_Freeze: `pip install cx_Freeze`
2. Update TCL/TK paths in `setup.py` to match your Python installation
3. Run: `python setup.py build`

## License

This project is open source. Feel free to use and modify as needed.
