from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api/notes', views.NoteViewSet)

urlpatterns = [
    path('list/', views.notes_list, name='notes_list'),
    path('create/', views.create_note, name='create_note'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('', include(router.urls)),
]
