# Python Image Resizer

A simple Python script that resizes images using OpenCV. It scales an input image to a specified percentage of its original dimensions and saves the result as a new file.

## Features

- Resizes images by a configurable scale percentage
- Preserves aspect ratio based on original width and height
- Uses OpenCV for fast, reliable image processing
- Outputs resized image as a new PNG file

## Requirements

- Python 3.x
- OpenCV (`opencv-python`)

Install dependencies:
```bash
pip install opencv-python
```

## Usage

```bash
git clone https://github.com/AhadAhmad0/Python-Image-Resizer.git
cd Python-Image-Resizer
python Image_Resizer.py
```

Place your source image in the project folder and update the `source` variable in the script with its filename. The resized output will be saved as `newImage.png`.

## How It Works

The script reads the source image, calculates new dimensions based on `scale_percent`, resizes it using `cv2.resize()`, and writes the result to disk.

## Author

**Ahad Ahmad** — [@AhadAhmad0](https://github.com/AhadAhmad0)
