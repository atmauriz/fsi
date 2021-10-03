from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=120, blank=True, null=True)
    content = models.TextField()

    def __str__(self):
        return self.title
