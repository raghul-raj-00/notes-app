from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('api/notes', views.NoteViewSet, basename='note')

urlpatterns = [
    path('', views.note_list,      name='note_list'),
    path('create/', views.create_note,  name='create_note'),
    path('edit/<int:pk>/', views.edit_note,    name='edit_note'),
    path('delete/<int:pk>/', views.delete_note, name='delete_note'),
    path('login/',  views.login_user,  name='login'),
    path('signup/', views.signup,      name='signup'),
    path('logout/', views.logout_user, name='logout'),
]

urlpatterns += router.urls
