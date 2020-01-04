from django.db import models
from django.utils.datetime_safe import datetime


class News(models.Model):
    photo = models.ImageField(upload_to='images/', default='images/default.jpg')
    title = models.CharField(max_length=255)
    description = models.TextField()
    news_data = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.title} {self.news_data}'