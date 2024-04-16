import os 
import subprocess
import acapellify

def process_video(video_path):
    old_audio = os.path.basename(video_path).split(".")[0] + ".m4a"
    subprocess.run(['ffmpeg', '-y', '-i', video_path, '-vn', '-acodec', 'copy', old_audio])

    new_audio = acapellify.acapellify(old_audio)

    new_video = f"acap_{video_path}"
    subprocess.call(['ffmpeg', '-y', '-i', video_path, '-i', new_audio, '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-strict', 'experimental', f"static/{new_video}"])
    return new_video