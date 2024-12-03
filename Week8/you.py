from pytube import YouTube

# Enter the YouTube video URL
url = "https://www.youtube.com/watch?v=dQw4w9W"

# Create a YouTube object with the URL
yt = YouTube(url)

# Select the highest resolution video
video = yt.streams.get_highest_resolution()

# Set the output directory and filename
output_dir = "/storage/emulated/0/Documents/"
filename = yt.title+".mp4"

# Download the video
video.download(output_dir, filename)

print(f"Download complete: {filename}")