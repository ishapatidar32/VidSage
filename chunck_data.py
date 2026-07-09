import os 
import whisper
import json


model = whisper.load_model("small")
audios = os.listdir("audios_trimmed")
for audio in audios:
    number = audio.split("_")[0]
    title  = audio.split("_")[1][:-4]
    result = model.transcribe(audio = f"audios_trimmed/{audio}", 
                              language="hi",
                              task="translate",
                              word_timestamps=False )
    chunk =[]
    for segment in result["segments"]:
        chunk.append({"number": number, "title":title, "start": segment["start"], "end": segment["end"], "text": segment["text"]})
    chunks_with_metadata = {"chunks": chunk, "text": result["text"]}
    with open(f"jsons_trimmed/{audio}.json", "w") as f:
        json.dump(chunks_with_metadata,f)