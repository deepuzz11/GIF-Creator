from moviepy.editor import VideoFileClip, ImageClip
import os

def create_gif_from_video(video_path, gif_path, start_time=0, end_time=None, fps=10):
    try:
        # Load the video clip
        video_clip = VideoFileClip(video_path)
        
        # Get the duration of the video
        video_duration = video_clip.duration

        # Set end time if not provided
        if end_time is None:
            end_time = video_duration
        elif end_time > video_duration:
            end_time = video_duration

        # Trim the video clip
        trimmed_clip = video_clip.subclip(start_time, end_time)

        # Generate the GIF
        trimmed_clip.write_gif(gif_path, fps=fps)

        # Close the video clip
        video_clip.close()

        print("GIF created successfully from video!")

    except Exception as e:
        print("Error occurred while creating GIF from video:", e)

def create_gif_from_image(image_path, gif_path, duration=1, fps=10):
    try:
        # Load the image clip
        image_clip = ImageClip(image_path, duration=duration)

        # Generate the GIF
        image_clip.write_gif(gif_path, fps=fps)

        print("GIF created successfully from image!")

    except Exception as e:
        print("Error occurred while creating GIF from image:", e)

def get_float_input(prompt):
    while True:
        try:
            user_input = float(input(prompt))
            return user_input
        except ValueError:
            print("Please enter a valid number.")

def main():
    file_type = input("Enter the file type to create GIF from (video/image): ").lower()
    
    if file_type == "video":
        video_path = input("Enter the path to the input video file: ")
        if not os.path.isfile(video_path):
            print("Error: Input video file does not exist.")
            return

        gif_path = input("Enter the path for the output GIF file (e.g., output.gif): ")

        start_time = get_float_input("Enter the start time (in seconds) for the GIF: ")
        end_time = get_float_input("Enter the end time (in seconds) for the GIF (leave blank for full duration): ")

        fps = get_float_input("Enter the frame rate (frames per second) for the GIF: ")

        create_gif_from_video(video_path, gif_path, start_time=start_time, end_time=end_time, fps=fps)
    
    elif file_type == "image":
        image_path = input("Enter the path to the input image file: ")
        if not os.path.isfile(image_path):
            print("Error: Input image file does not exist.")
            return

        gif_path = input("Enter the path for the output GIF file (e.g., output.gif): ")

        duration = get_float_input("Enter the duration (in seconds) for each frame in the GIF: ")
        fps = get_float_input("Enter the frame rate (frames per second) for the GIF: ")

        create_gif_from_image(image_path, gif_path, duration=duration, fps=fps)
    
    else:
        print("Invalid file type. Please choose either 'video' or 'image'.")

if __name__ == "__main__":
    main()
