# 📝 Notes App

A secure Django-based Notes Application with an integrated Retrieval-Augmented Generation (RAG) pipeline. Users can create, manage, and organize notes while leveraging AI-powered summarization and context-aware question answering. The application uses PostgreSQL for data storage, vector embeddings for semantic retrieval, and an LLM to generate accurate responses based on retrieved note content.

---

## 🚀 Features

- 🔐 User Authentication (Register, Login, Logout)
- 📝 Create, Read, Update, Delete (CRUD) Notes
- 🤖 AI-powered Note Summarization
- 🔍 RAG-based Question Answering
- 📚 Semantic Search using Vector Embeddings
- 🗄️ PostgreSQL Database
- 🐳 Docker & Docker Compose Support
- 🎨 Responsive and Clean User Interface
- 🔒 Session-based Authentication
- ⚡ Fast and Lightweight Django Application

---

## 🛠️ Tech Stack

### Backend
- Python
- Django

### Database
- PostgreSQL

### AI/RAG
- LLM API for Note Summarization
- Vector Embeddings
- Pinecone (Vector Database)

### DevOps
- Docker
- Docker Compose

### Frontend
- HTML
- CSS


---

## 📂 Project Structure

```
notes-app/
│── account/
│── notes/
│── static/
│── templates/
│── firstdjango/
│── docker-compose.yml
│── Dockerfile
│── manage.py
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/raghul-raj-00/notes-app.git

cd notes-app
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root.

Example:

```env
SECRET_KEY=your_secret_key

DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=db
DB_PORT=5432

LLM_API_KEY=your_api_key
```

---

### 5. Run Database Migrations

```bash
python manage.py migrate
```

---

### 6. Start Development Server

```bash
python manage.py runserver
```

Open

```
http://127.0.0.1:8000/
```

---

# 🐳 Running with Docker

Build and start containers

```bash
docker compose up --build
```

Run in detached mode

```bash
docker compose up -d
```

Stop containers

```bash
docker compose down
```

---



## 💡 AI Summarization

The application can summarize lengthy notes using an LLM API.

Workflow:

```
User Note
      │
      ▼
LLM API
      │
      ▼
Generated Summary
      │
      ▼
Displayed in the Application
```

---
## 🧠 RAG Pipeline

The application includes a Retrieval-Augmented Generation (RAG) pipeline that enables users to ask questions about their notes and receive context-aware answers.

### Workflow

1. User submits a question.
2. The question is converted into a vector embedding.
3. Similar note chunks are retrieved from the vector database.
4. Retrieved context is combined with the user's question.
5. The LLM generates an answer using only the retrieved context.
6. The generated response is displayed to the user.

```
User Question
      │
      ▼
Embedding Model
      │
      ▼
Vector Database
 (Semantic Search)
      │
Retrieved Chunks
      │
      ▼
Prompt + Context
      │
      ▼
LLM
      │
      ▼
Generated Answer
```
---
## 📖 Usage

1. Register a new account.
2. Login securely.
3. Create a note.
4. Edit or delete notes.
5. Generate AI summaries for lengthy notes.
6. Ask questions related to your stored notes using the RAG chatbot.
7. Logout.

---

## 🔒 Authentication

- User Registration
- User Login
- User Logout
- Session Authentication
- Protected Routes

---

## 📌 Future Improvements

- Multi-document RAG
- Hybrid Search (Keyword + Semantic)
- Rich Text Editor
- Note Categories
- Tags
- Search & Filter
- File Attachments
- Note Sharing
- Email Verification

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push to your branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Raghul Raj**

GitHub: https://github.com/raghul-raj-00
