from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    # create attributes
    title = models.CharField(max_length=100)  # title that is a string
    content = models.TextField()  # same as CharField but lines of text
    date_posted = models.DateTimeField(default=timezone.now)
    # if the user gets deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
