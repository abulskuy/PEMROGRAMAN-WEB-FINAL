from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm  
from django.core.paginator import Paginator 

# Fungsi untuk menampilkan daftar buku
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_list(request):
    query = request.GET.get('q')  # Ambil query pencarian dari URL
    if query:
        books = Book.objects.filter(title__icontains=query)  # Filter berdasarkan judul
    else:
        books = Book.objects.all()  # Ambil semua buku

    paginator = Paginator(books, 5)  # Tampilkan 5 buku per halaman
    page_number = request.GET.get('page')  # Ambil nomor halaman dari URL
    page_obj = paginator.get_page(page_number)  # Dapatkan objek halaman
    return render(request, 'books/book_list.html', {'page_obj': page_obj, 'query': query})

# Fungsi untuk membuat buku baru
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})

# Fungsi untuk mengedit buku
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form})

# Fungsi untuk menghapus buku
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})