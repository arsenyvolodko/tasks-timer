from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.DateTimeField(null=True, blank=True, default=None)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
