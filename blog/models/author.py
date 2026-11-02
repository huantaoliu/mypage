from django.core import validators
from django.db import models


class Author(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_address = models.EmailField(unique=True)
