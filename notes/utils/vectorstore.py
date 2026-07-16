import os
from dotenv import load_dotenv
from pinecone import Pinecone
load_dotenv()

pc=Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index=pc.Index("notes-rag")
print(pc.list_indexes())

#fn for storing the embedding from get_embeddinng
def store_embedding(user_id,note_id,embedding,chunk_id,chunk_text):
    vector_id=f"{user_id}_{note_id}_{chunk_id}"
    index.upsert(vectors=[{"id":vector_id,"values":embedding,"metadata":{"user_id":user_id,"note_id":note_id,"chunk_text":chunk_text,}}],namespace="")
    
def delete_note_vectors(user_id,note_id):
    # Delete all vectors associated with the note
    index.delete(filter={"user_id":user_id,"note_id":note_id},namespace="")
    
def search_vectors(query_embedding,user_id,top_k=5):
    return index.query(vector=query_embedding,top_k=top_k,include_metadata=True,filter={"user_id":user_id},namespace="")
#next is retrival.py