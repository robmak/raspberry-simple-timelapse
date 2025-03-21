import subprocess

index = 0
while True:
    #print("capturing images.")
    subprocess.run(["rpicam-still", "-n", "-c", "config.txt", "-o", "/var/tmp/ringcam/image%04d.jpg"])
    videofile = f'/var/tmp/ringcam/timelapse{index}.mp4'
    #print(f'converting video {videofile}')
    #subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "quiet", "-y", "-r", "10", "-f", "image2", "-pattern_type","glob", "-i", "/var/tmp/ringcam/image*.jpg", "-s", "1280x720", "-an", "-vf", "drawtext=fontfile=roboto.ttf:fontsize=36:fontcolor=yellow:text='%{pts\:gmtime\:1575526882\:%A, %d, %B %Y %I\\\:%M\\\:%S %p}'", "-vcodec", "libx264", "-tune", "film", "-profile:v", "high", "-crf", "28", "-movflags", "+faststart", videofile])
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "quiet", "-y", "-r", "15", "-f", "image2", "-pattern_type","glob", "-i", "/var/tmp/ringcam/image*.jpg", "-s", "1280x720", "-an", "-vf", "drawtext=fontfile=roboto.ttf:fontsize=14:fontcolor=yellow:text='%{localtime}'", "-vcodec", "libx264", "-tune", "film", "-profile:v", "high", "-crf", "29", "-movflags", "+faststart", videofile])
    index = (index + 1) % 15

