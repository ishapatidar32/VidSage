# Converts the videos to mp3 
# but i have not use this code 
# us ffmpeg and yt-dlp 
import os 
import subprocess

#files = os.listdir("videos") 
#for file in files: 
   # tutorial_number = file.split(" [")[0].split(" #")[1]
   # file_name = file.split(" ｜ ")[0]
    #print( tutorial_number,  file_name)
   # subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios/{tutorial_number}_{file_name}.mp3"])

input_folder = "lectures"
output_folder = "audios_trimmed"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
mp3_files = [f for f in os.listdir(input_folder) if f.endswith(".mp3")]
print(f"Found {len(mp3_files)} MP3 files")
for mp3 in mp3_files:
    input_path = os.path.join(input_folder, mp3)
    output_path = os.path.join(output_folder, mp3)
    
    print(f"Trimming: {mp3}")
    
    subprocess.run([
        "ffmpeg",
        "-i", input_path,      # input file
        "-t", "180",           # 180 seconds = 3 minutes
        "-acodec", "copy",     # no re-encoding, just cut (fast)
        output_path,
        "-y"                   # overwrite if exists
    ])
print(f" Done: {mp3}")