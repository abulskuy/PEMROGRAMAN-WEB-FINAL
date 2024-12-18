from django.urls import path
from .views import book_list, book_create, book_update, book_delete

urlpatterns = [
    path('', book_list, name='book_list'),  # URL untuk daftar buku
    path('book/new/', book_create, name='book_create'),  # URL untuk membuat buku baru
    path('book/<int:pk>/edit/', book_update, name='book_update'),  # URL untuk mengedit buku
    path('book/<int:pk>/delete/', book_delete, name='book_delete'),  # URL untuk menghapus buku
]