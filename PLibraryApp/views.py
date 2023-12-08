from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book
from django.urls import reverse

def helloView(request):
    books = Book.objects.all()
    return render(request, 'booklist.html', {'books': books})

def addBookView(request):
    return render(request, "addbook.html")

def addBook(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        price = request.POST['price']
        synopsis = request.POST['synopsis']
        
        book = Book(title=title, author=author, price=price, synopsis=synopsis)
        book.save()
        
        
        return HttpResponseRedirect('helloView')
        # success_message = f"{book.title} was added successfully"  # Correct formatting of the success message

        # # Redirect to the root URL with the success message as a query parameter
        # return HttpResponseRedirect(reverse('helloView') + f'?success_message={success_message}')
    
def editBookView(request):
    book = Book.objects.get(id=request.GET.get('bookid'))
    return render(request, "editbook.html", {'book': book}) 

def editBook(request):
    
    pass