from django import forms
from manga import models
from manga.parser import parser


class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ("Manga", "Manga"),
        ("manga", "manga")
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)
    class meta:
        fields = [
            "media_type",
        ]


    def parser_data(self):
        if self.data["media_type"] == "Manga":
            anime_data = parser()
            for i in anime_data:
                models.Manga.objects.create(**i)

        elif self.data["media_type"] == "manga":
            books_data = parser()
            for i in books_data:
                models.Manga.objects.create(**i)