# Generated by Django 4.1.6 on 2023-07-21 02:25

import MovieApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieApp', '0005_remove_review_score_review_rated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rated',
            field=models.IntegerField(default=1, validators=[MovieApp.models.validate_score]),
        ),
    ]