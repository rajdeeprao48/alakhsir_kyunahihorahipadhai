import time
import webbrowser

# Set the YouTube video URL
video_url = "https://www.youtube.com/watch?v=sTaEwwHOzjc"  # Replace with your video URL

# Set the delay time in seconds (10 minutes = 600 seconds)
delay_time = 600

# Initialize a flag to track if the video has been played
video_played = False

while True:
    # Check if the video has not been played yet
    if not video_played:
        # Print a message to indicate the program is running
        print("Program started. Video will play in 10 minutes.")

        # Wait for the delay time
        time.sleep(delay_time)

        # Open the YouTube video in a web browser
        webbrowser.open(video_url)

        # Set the flag to indicate the video has been played
        video_played = True

        print("Video is now playing!")
    else:
        # If the video has already been played, exit the loop
        break
