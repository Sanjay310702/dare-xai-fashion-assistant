import pandas as pd
import chromadb
import os

def build_vector_database():
    csv_path = "outfits.csv"
    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found!")
        return

    # Load data and handle missing strings safely
    df = pd.read_csv(r"C:/Users/sanjay/ML-TASK/outfits.csv")
    df = df.fillna("")

    print(f"Loaded {len(df)} outfits. Initializing Vector Database...")

    # Initialize a local persistent ChromaDB client
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    
    # Create or get the collection
    collection = chroma_client.get_or_create_collection(name="fashion_assistant")

    documents = []
    metadatas = []
    ids = []

    for index, row in df.iterrows():
        # Combine the items neatly
        items_description = f"Topwear/Hero: {row['hero']}."
        if row['second']:
            items_description += f" Bottomwear: {row['second']}."
        if row['layer']:
            items_description += f" Layering: {row['layer']}."
        if row['footwear']:
            items_description += f" Footwear: {row['footwear']}."
        if row['accessory_1']:
            items_description += f" Accessories include {row['accessory_1']}."

        # Create a rich text package that represents this whole outfit semantically
        enriched_text = (
            f"A {row['gender']}'s {row['wear_type']} outfit ideal for a {row['occasion']} occasion. "
            f"The style theme is {row['theme']} using a {row['palette']} color palette. "
            f"Outfit breakdown: {items_description} "
            f"Stylist Reasoning: {row['stylist_rationale']}"
        )

        documents.append(enriched_text)
        
        # Store all original columns as metadata so we can display them in our UI later
        metadatas.append({
            "outfit_id": str(row['outfit_id']),
            "gender": row['gender'],
            "wear_type": row['wear_type'],
            "occasion": row['occasion'],
            "theme": row['theme'],
            "hero": row['hero'],
            "second": row['second'],
            "layer": row['layer'],
            "footwear": row['footwear'],
            "accessory_1": row['accessory_1'],
            "palette": row['palette'],
            "image_files": row['image_files'],
            "stylist_rationale": row['stylist_rationale']
        })
        
        ids.append(str(row['outfit_id']))

    # Upsert items into ChromaDB (it handles default embeddings automatically)
    collection.upsert(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )

    print(f"Successfully indexed {len(documents)} fashion outfits into ChromaDB vector space!")

if __name__ == "__main__":
    build_vector_database()