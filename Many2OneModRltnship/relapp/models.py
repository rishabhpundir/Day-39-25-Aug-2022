from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=100)
    post_publication_date = models.DateField()

    def __str__(self):
        return self.post_title