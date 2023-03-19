import cv2
import numpy as np

# Function to convert a file to a video
def convert_to_video(file_path, video_path):
    # Read the file as bytes
    with open(file_path, "rb") as f:
        file_bytes = f.read()

    # Set the dimensions of the video frames based on the file size
    frame_height = int(np.sqrt(len(file_bytes)))
    frame_width = int(len(file_bytes) / frame_height) + 1

    # Reshape the file bytes into a 2D numpy array
    file_array = np.frombuffer(file_bytes, dtype=np.uint8)
    file_array.resize((frame_height, frame_width))

    # Create the video writer object
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_writer = cv2.VideoWriter(video_path, fourcc, 24, (frame_width, frame_height))

    # Write each frame to the video
    for i in range(frame_height):
        # Convert the row of the file array to a 2D numpy array
        frame = np.array([file_array[i, :]])
        frame.resize((frame_height, frame_width))

        # Convert the frame to BGR format for OpenCV
        frame_bgr = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

        # Write the frame to the video
        video_writer.write(frame_bgr)

    # Release the video writer object
    video_writer.release()

# Function to convert a video to a file
def convert_to_file(video_path, output_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Initialize an empty list to store the frames
    frames = []

    # Loop through each frame in the video
    while cap.isOpened():
        # Read the frame
        ret, frame = cap.read()
        # If the frame was successfully read, convert it to grayscale and add it to the list of frames
        if ret:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frames.append(gray_frame)
        # If the frame couldn't be read, break the loop
        else:
            break

    # Release the video capture object
    cap.release()

    # Convert the list of frames to a 2D numpy array
    file_array = np.concatenate(frames, axis=0)

    # Convert the file array to bytes
    file_bytes = file_array.tobytes()

    # Write the bytes to a file
    with open(output_path, "wb") as f:
        f.write(file_bytes)

# Example usage
# Convert a file to a video
file_path = "path/to/your/file"
video_path = "path/to/output/video.mp4"
convert_to_video(file_path, video_path)

# Convert the video back to a file
output_path = "path/to/output/file"
convert_to_file(video_path, output_path)
