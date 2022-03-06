from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    date_birth = models.DateField()
    story_author = models.TextField()
    interesting_facts = models.CharField(max_length=50)

class Book(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    duration = models.PositiveIntegerField(null=True)

class Review(models.Model):
    text = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)



