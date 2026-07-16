from .chunking import chunk_text
from .embeddings import get_embedding
from .vectorstore import store_embedding, delete_note_vectors
from .retrieval import retrieve_chunks
from .ai import generate_answer

def index_note(note,is_update=False):
    if is_update:
        delete_note_vectors(note.user.id,note.id)
    
    chunks=chunk_text(note.content)
    for idx,chunk in enumerate(chunks):
        embedding=get_embedding(chunk)
        store_embedding(note.user.id,note.id,embedding,idx,chunk)

def ask_question(question,user_id):
    qchunk=retrieve_chunks(question,user_id)
    context="\n".join(qchunk)
    response=generate_answer(question,context)
    return response
#next to add functionalites in views.py and adding model in ai.py for response