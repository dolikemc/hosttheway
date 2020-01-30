from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    description = models.TextField(max_length=2048)
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
