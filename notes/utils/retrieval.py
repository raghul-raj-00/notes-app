#task gonna do in the file is converting question to embedding and then do searching with notes embedding and then passing the result chuck to ai for actual response
from .embeddings import get_embedding
from .vectorstore import search_vectors

def retrieve_chunks(question,user_id):
    query_embedding=get_embedding(question)
    results=search_vectors(query_embedding,user_id)
    chunks=[]
    for matches in results['matches']:
        chunks.append(matches['metadata']['chunk_text'])
    return chunks
