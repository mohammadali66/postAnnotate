from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

#----------------------------------------------------------------------------------------------------------------------
class Post(models.Model):
    title   = models.CharField(max_length=100)
    author  = models.ForeignKey(User, on_delete=models.CASCADE)
    tags    = models.ManyToManyField(Tag)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
