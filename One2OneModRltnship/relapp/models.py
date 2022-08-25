from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Page(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    page_name = models.CharField(max_length=100)
    page_description = models.CharField(max_length=200)

    def __str__(self):
        return self.page_name