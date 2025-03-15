import subprocess

index = 0
while True:
    print("capturing images.")
    subprocess.run(["rpicam-still", "-n", "-c", "config.txt", "-o", "/var/tmp/ringcam/image%04d.jpg"])
    videofile = f'/var/tmp/ringcam/timelapse{index}.mp4'
    print(f'converting video {videofile}')
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "quiet", "-y", "-r", "10", "-f", "image2", "-pattern_type","glob", "-i", "/var/tmp/ringcam/image*.jpg", "-s", "1280x720", "-an", "-vcodec", "libx264", "-tune", "film", "-profile:v", "high", "-crf", "28", "-movflags", "+faststart", videofile])
    index = (index + 1) % 5

