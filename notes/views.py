from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Note
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import NoteSerializer
from .utils.ai import summarize_text
# ---------- auth ----------
def signup(request):
    if request.method == 'POST':
        u, p1, p2 = request.POST['username'], request.POST['password1'], request.POST['password2']
        if p1 != p2:
            messages.error(request, 'Passwords do not match'); return redirect('signup')
        if User.objects.filter(username=u).exists():
            messages.error(request, 'Username taken'); return redirect('signup')
        User.objects.create_user(username=u, password=p1)
        messages.success(request, 'Account created, please log-in'); return redirect('login')
    return render(request, 'notes_register.html')

def login_user(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user: login(request, user); return redirect('note_list')
        messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

# ---------- CRUD ----------
@login_required
def note_list(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'note_list.html', {'notes': notes})

@login_required
def create_note(request):
    if request.method == 'POST':
        Note.objects.create(user=request.user,
                            title=request.POST['title'],
                            content=request.POST['content'])
        return redirect('note_list')
    return render(request, 'note_form.html', {'note': None})

@login_required
def edit_note(request, pk):
    note = get_object_or_404(Note, id=pk, user=request.user)
    if request.method == 'POST':
        note.title, note.content = request.POST['title'], request.POST['content']
        note.save(); return redirect('note_list')
    return render(request, 'note_form.html', {'note': note})

@login_required
def delete_note(request, pk):
    note = get_object_or_404(Note, id=pk, user=request.user)
    if request.method == 'POST':
        note.delete(); return redirect('note_list')
    return render(request, 'confirm_delete.html', {'note': note})
@login_required
def summarize_note(request, pk):
    note = get_object_or_404(Note, id=pk, user=request.user)
    summary = summarize_text(note.content)
    note.summary = summary
    note.save()
    messages.success(request, "AI Summary is generated!")
    return redirect('note_list')


# ---------- API ----------
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
