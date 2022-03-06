from django.test import TestCase
from datetime import date
from . import models
from django.test import Client
from django.contrib.auth.models import User


class ReviewsTestModels(TestCase):
    # def test_update_model(self):
    #     review = {"text": "Oikawa",
    #               "created_date": date.today(),
    #               "age": 34,
    #               }
    #     reviews = models.Review.objects.create(**review)
    #     new_create_date = date.today()
    #     reviews.created_date = new_create_date
    #     reviews.save()
    #     reviews.refresh_from_db()
    #     self.assertEqual(reviews.created_date, new_create_date)
    #
    # def test_delete_model(self):
    #     review = {"text": "Oikawa",
    #               "created_date": date.today(),
    #               "age": 34,
    #               }
    #     reviews = models.Review.objects.create(**review)
    #     review_id = reviews.id
    #     reviews.delete()
    #     with self.assertRaises(models.Review.DoesNotExist):
    #         models.Review.objects.get(id=review_id)

    # def test_model_create_success(self):
    #     review = {"text": "Oikawa",
    #               "created_date": date.today(),
    #               "age": 12,
    #               }
    #     reviews = models.Review.objects.create(**review)
    #     self.assertEqual(reviews.text, review['text'])
    #     self.assertEqual(reviews.created_date, review['created_date'])
    #     self.assertEqual(reviews.age, review['age'])

    def test_model_create_fail(self):
        review = {"text": "Oikawa",
                  "created_date": date.today(),
                  "age": "HH"
                  }
        with self.assertRaises(ValueError):
            reviews = models.Review.objects.create(**review)


class BookTestModels(TestCase):
    def test_model_create_success(self):
        book = {
            "title": "Blich",
            "description": "Test Desk",
            "image": "image.png",
            "created_date": date.today(),
            "updated_date": date.today(),
            "duration": 23,
        }
        books = models.Book.objects.create(**book)
        self.assertEqual(books.title, book['title'])
        self.assertEqual(books.description, book['description'])
        self.assertEqual(books.image, book['image'])
        self.assertEqual(books.created_date, book['created_date'])
        self.assertEqual(books.updated_date, book['updated_date'])
        self.assertEqual(books.duration, book['duration'])

    def test_model_create_fail(self):
        book = {
            "title": "21",
            "description": "len",
            "image": "12",
            "created_date": date.today(),
            "updated_date": date.today(),
            "duration": "Long",
        }

        with self.assertRaises(ValueError):
            book = models.Book.objects.create(**book)

    def test_update_model(self):
        book = {
            "title": "One Piece",
            "description": "Test Desk",
            "image": "image.png",
            "created_date": date.today(),
            "updated_date": date.today(),
            "duration": 23,
        }
        books = models.Book.objects.create(**book)
        new_title = "Blich"
        books.title = new_title
        books.save()
        books.refresh_from_db()
        self.assertEqual(books.title, new_title)
        new_description = "Better Anime"
        books.description = new_description
        books.save()
        books.refresh_from_db()
        self.assertEqual(books.description, new_description)
        new_image = "381758.jpg"
        books.image = new_image
        books.save()
        books.refresh_from_db()
        self.assertEqual(books.image, new_image)
        new_created_date = date.today()
        books.created_date = new_created_date
        books.save()
        books.refresh_from_db()
        self.assertEqual(books.created_date, new_created_date)
        new_update_date = date.today()
        books.updated_date = new_update_date
        books.save()
        books.refresh_from_db()
        self.assertEqual(books.updated_date, new_update_date)
        new_duration = 5
        books.duration = new_duration
        books.save()
        books.refresh_from_db()
        self.assertEqual(books.duration, new_duration)

    def test_delete_model(self):
        book = {
            "title": "One Piece",
            "description": "Test Desk",
            "image": "image.png",
            "created_date": date.today(),
            "updated_date": date.today(),
            "duration": 23,
        }
        books = models.Book.objects.create(**book)
        book_id = books.id
        books.delete()
        with self.assertRaises(models.Book.DoesNotExist):
            models.Book.objects.get(id=book_id)


class TestView(TestCase):
    def test_get_success(self):
        book = {
            "title": "One Piece",
            "description": "Test Desk",
            "image": "image.png",
            "created_date": date.today(),
            "updated_date": date.today(),
            "duration": 23,
        }
        books = models.Book.objects.create(**book)
        client = Client()
        user = User.objects.create(username='Username')
        client.force_login(user)
        response = client.get(path=f"/books/{books.id}/")
        self.assertEqual(response.status_code, 200)
