from django.http import Http404, HttpResponse
from django.shortcuts import reverse, redirect, render, get_object_or_404
from django.views import generic
from . import models, forms


class BooksListView(generic.ListView):
    template_name = "book_list.html"
    queryset = models.Book.objects.all()
    context_object_name = 'book'


class BooksDetailViews(generic.DetailView):
    template_name = "book_detail.html"
    context_object_name = 'book'

    def get_object(self, **kwargs):
        books_id = self.kwargs.get("pk")
        return get_object_or_404(models.Book, pk=books_id)


class BooksCreateView(generic.CreateView):
    template_name = "add_book_list.html"
    form_class = forms.Book_form
    queryset = models.Book.objects.all()
    success_url = "/books/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BooksCreateView, self).form_valid(form=form)


class BooksUpDateView(generic.UpdateView):
    template_name = "books_update.html"
    form_class = forms.Book_form
    success_url = "/books/"

    def get_object(self, **kwargs):
        books_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, pk=books_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BooksUpDateView, self).form_valid(form=form)


class BooksDeleteView(generic.DeleteView):
    success_url = "/books/"
    template_name = "confirm_delete_book.html"

    def get_object(self, **kwargs):
        books_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, pk=books_id)


def add_books(request):
    method = request.method
    if method == "POST":
        form = forms.Book_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/books/")

    else:
        form = forms.Book_form()
    return render(request, "add_book_list.html", {"form": form})
