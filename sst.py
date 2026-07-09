import whisper
import json
# to chunking  one semple data 
model = whisper.load_model("small")

result = model.transcribe(audio = f"audios_trimmed/1_part1.mp3", 
                          language="hi",
                          task="translate",
                           word_timestamps=False )

 
chunks = []
for segment in result["segments"]:
    chunks.append({"start": segment["start"], "end": segment["end"], "text": segment["text"]})

chunks_with_metadata = {"chunks": chunks, "text": result["text"]}
with open("output.json", "w") as f:
    json.dump(chunks_with_metadata, f)
