from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, FormView
from . import models, forms


class AnimeView(ListView):
    model = models.Manga
    template_name = "manga/manga_list.html"
    context_object_name = "manga"

    def get_queryset(self):
        return models.Manga.objects.all()


class ParserAnimeView(FormView):
    template_name = "manga/manga_parser.html"
    form_class = forms.ParserForm
    success_url = "/manga/"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponseRedirect(self.success_url)
        else:
            return super(ParserAnimeView, self).post(request, *args, **kwargs)
