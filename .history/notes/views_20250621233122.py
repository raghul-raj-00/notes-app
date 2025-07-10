from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Note
from rest_framework import viewsets
from .serializers import NoteSerializer
from rest_framework.permissions import IsAuthenticated

# ---------- Auth Views ----------
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/notes/list/')
        else:
            return render(request, 'notes_login.html', {'error': 'Invalid credentials'})
    return render(request, 'notes_login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                return redirect('/login/')
            else:
                return render(request, 'register.html', {'error': 'Username already exists'})
        else:
            return render(request, 'notes_register.html', {'error': 'Passwords do not match'})
    return render(request, 'notes_register.html')

def logout_user(request):
    logout(request)
    return redirect('/login/')

# ---------- HTML CRUD Views ----------
def notes_list(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    notes = Note.objects.filter(user=request.user)
    return render(request, 'note_list.html', {'notes': notes})

def create_note(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Note.objects.create(user=request.user, title=title, content=content)
        return redirect('/notes/list/')
    return render(request, 'note_form.html')

# ---------- API ViewSet ----------
class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
