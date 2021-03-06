from django.db import models

# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length=255)

    about = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)

    last_modified = models.DateTimeField(auto_now=True)
