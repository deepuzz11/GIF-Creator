# GIF Creator

## Introduction

The GIF Creator Python script provides a convenient way to generate animated GIFs from either a video or an image file. With its intuitive command-line interface and customizable parameters, this script offers flexibility and ease of use for creating GIFs tailored to your requirements.

## Prerequisites

Before using the GIF Creator script, ensure you have the following prerequisites installed on your system:

- **Python 3.x**: The script is compatible with Python 3.x versions.
- **MoviePy library**: Install the MoviePy library using the following pip command:
  ```bash
  pip install moviepy
## Usage

Follow the steps below to use the GIF Creator script:

1. **Download the script**: Clone this repository or download the `gif_creator.py` script.

2. **Install prerequisites**: Ensure you have Python 3.x and the MoviePy library installed on your system.

3. **Run the script**: Open a terminal or command prompt, navigate to the directory containing `gif_creator.py`, and execute the script using the following command:
   ```bash
   python gif_creator.py
4. Follow the prompts to create GIFs using the GIF Creator script. The script will guide you through choosing the file type (video or image) and provide the necessary input parameters.

## Command-Line Arguments

The GIF Creator script accepts the following command-line arguments:

- `file_type`: Specifies whether to create a GIF from a video or an image. Enter either 'video' or 'image'.
- `video_path` (if `file_type` is 'video'): Path to the input video file.
- `image_path` (if `file_type` is 'image'): Path to the input image file.
- `gif_path`: Path for the output GIF file.
- `start_time` (optional): Start time (in seconds) for the GIF (applicable only for video files).
- `end_time` (optional): End time (in seconds) for the GIF (applicable only for video files).
- `duration` (optional): Duration (in seconds) for each frame in the GIF (applicable only for image files).
- `fps`: Frame rate (frames per second) for the GIF.

## License

The GIF creator script and all other programs within this repository are governed by the MIT License. You are granted the freedom to utilize them for educational purposes and to adapt them to suit your needs. However, please be advised that I do not assume any responsibility for the accuracy or reliability of these programs.
