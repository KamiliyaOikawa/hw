from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    GENDER_TYPE = (
        ("MALE", "MALE"),
        ("FEMALE", "FEMALE"),
        ("OTHER", "OTHER"),
        ("ANIMAL","ANIMAL"),
        ('PROGRAMMER','PROGRAMMER'),
        ("EKAI","EKAI"),
        ("JINN","JINN")
    )
    OCUPATIONC_HOICE = (
        ("STUDENT", "STUDENT"),
        ("WORKER", "WORKER"),
        ("JOBLESS", "JOBLESS"),
        ("RETIRED", "RETIRED"),
        ("MILLIONAIRE", "MILLIONAIRE")
    )
    phone_number = models.CharField("phone-number", max_length=60, unique=True)
    gender = models.CharField(choices=GENDER_TYPE,max_length=60 ,verbose_name="Гендер")
    age = models.PositiveIntegerField()
    occupation = models.CharField(choices=OCUPATIONC_HOICE, max_length=80)
    national = models.TextField()

