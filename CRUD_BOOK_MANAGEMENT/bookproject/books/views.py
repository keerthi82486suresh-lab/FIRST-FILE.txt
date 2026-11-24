from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm, PriceUpdateForm


# READ - Display all books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html',
                  {'books': books})


# CREATE - Add new book
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()

    return render(request, 'books/add_book.html',
                  {'form': form})


# UPDATE - Update book price
def update_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        form = PriceUpdateForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = PriceUpdateForm(instance=book)

    return render(request, 'books/update_book.html',
                  {'form': form, 'book': book})


# DELETE - Delete book
def delete_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.delete()
        return redirect('book_list')

    return render(request, 'books/delete_book.html',
                  {'book': book})