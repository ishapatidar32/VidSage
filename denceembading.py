import ollama
import json 
import os 


print("Loading JSON file...")
with open("output_processed.json", "r", encoding="utf-8") as f:
    data = json.load(f)
print(f"Total chunks: {len(data['chunks'])}")



print("Generating embedding for each chunk...")
embedded_chunks = []
for i, chunk in enumerate(data['chunks']):
    print(f"Processing chunk {i+1}/{len(data['chunks'])}")
    response = ollama.embeddings(
        model="nomic-embed-text",
        prompt=chunk["text"]    
    )
    embedded_chunks.append({
        "start" : chunk["start"],
        "end" : chunk["end"],
        "text" : chunk["text"],
        "keywords":chunk["keywords"],
        "entities":chunk["entities"],
        "embedding" : response["embedding"] #768 number 
    })
    print(f"✅ Chunk {i+1}/{len(data['chunks'])} done")
final_output = {
    "text" : data["text"], 
    "chunks": embedded_chunks
}
if not os.path.exists("embedding"):
    os.makedirs("embedding")

with open("1part_embedded.json" , "w" , encoding="utf-8")as f:
     json.dump(final_output, f, indent=2, ensure_ascii=False)
print(f"done")
print("\nPreview of first chunk:")
first = embedded_chunks[0]
print(f"Start    : {first['start']}s")
print(f"End      : {first['end']}s")
print(f"Text     : {first['text'][:80]}...")
print(f"Keywords : {first['keywords']}")
print(f"Entities : {first['entities']}")
print(f"Embedding: {first['embedding'][:5]}...")  # first 5 values
print(f"Vector size: {len(first['embedding'])}")  # should be 768
