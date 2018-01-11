from django.db import models

# Create your models here.
import datetime

from django.db import models
from django.utils import timezone

class Book(models.Model):
    book_title = models.CharField(max_length=200)
    book_length_pages = models.IntegerField(default=0, blank=True)
    book_length_words = models.IntegerField(default=0, blank=True)
    book_pub_date = models.DateTimeField(default=timezone.now())
    def __str__(self):
        return self.book_title

class Page(models.Model):
    pub_date = models.DateTimeField('date published')
    user_page_input = models.IntegerField()
    def __str__(self):
        return self.user_page_input
