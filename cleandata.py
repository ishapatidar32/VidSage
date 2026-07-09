import spacy
import json
import re

# Load spacy model
nlp = spacy.load("en_core_web_sm")

# ─── Clean text function ──────────────────────────────────────────
def clean_text(text):
    
    # Remove filler words
    fillers = [
        r'\buh\b', r'\bum\b', r'\byou know\b',
        r'\bbasically\b', r'\bokay\b', r'\bright\b',
        r'\bactually\b'
    ]
    for filler in fillers:
        text = re.sub(filler, '', text, flags=re.IGNORECASE)
    
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

# ─── Extract keywords ─────────────────────────────────────────────
def extract_keywords(text):
    doc = nlp(text)
    
    keywords = list(set([
        token.text for token in doc
        if token.pos_ in ["NOUN", "PROPN"]
        and not token.is_stop
        and len(token.text) > 2
    ]))
    
    entities = list(set([ent.text for ent in doc.ents]))
    
    return keywords, entities

# ─── Main ─────────────────────────────────────────────────────────

# Step 1: Load existing JSON file from whisper
print("Loading JSON file...")
with open("output.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Total chunks loaded: {len(data['chunks'])}")

# Step 2: Process each chunk with spaCy
print("Processing with spaCy...")
processed_chunks = []

for i, chunk in enumerate(data["chunks"]):
    
    # Clean text
    cleaned = clean_text(chunk["text"])
    
    # Skip very short chunks
    if len(cleaned) < 10:
        continue
    
    # Extract keywords
    keywords, entities = extract_keywords(cleaned)
    
    processed_chunks.append({
        "start"   : chunk["start"],
        "end"     : chunk["end"],
        "text"    : cleaned,
        "keywords": keywords,
        "entities": entities
    })
    
    print(f"✅ Chunk {i+1}/{len(data['chunks'])} done")

# Step 3: Build final output
final_output = {
    "text"  : clean_text(data["text"]),
    "chunks": processed_chunks
}

# Step 4: Save processed file
with open("output_processed.json", "w", encoding="utf-8") as f:
    json.dump(final_output, f, indent=2, ensure_ascii=False)

print(f"\n✅ Done! Total chunks processed: {len(processed_chunks)}")
print("Saved to output_processed.json")

# Step 5: Preview first 2 chunks
print("\nPreview:")
for chunk in processed_chunks[:2]:
    print(f"\nTime     : {chunk['start']}s - {chunk['end']}s")
    print(f"Text     : {chunk['text']}")
    print(f"Keywords : {chunk['keywords']}")
    print(f"Entities : {chunk['entities']}")