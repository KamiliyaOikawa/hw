# Generated by Django 4.0 on 2022-03-06 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_book_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
