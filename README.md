# gif_resizer

GifResizer is a simple command-line tool for resizing GIFs while maintaining their animation. It uses the Python `Pillow` library to handle GIF resizing.

## Features
- Resize GIFs to any width and height while maintaining animation.
- Preserve transparency and frame durations for smooth playback.

## Prerequisites

- Python 3.6 or later
- `Pillow` library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/GifResizer.git
    cd GifResizer
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To resize a GIF, use the following command:

### Example:
```bash
python gif_resizer/resize_gif.py <input_path> <output_path> <width> <height>
python gif_resizer/resize_gif.py giphy.gif resized_gif.gif 500 500
```

### Parameters:
- `<input_path>`: The path to the original GIF you want to resize.
- `<output_path>`: The path where the resized GIF should be saved.
- `<width>`: The new width of the GIF in pixels.
- `<height>`: The new height of the GIF in pixels.