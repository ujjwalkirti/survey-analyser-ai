from django.db import models
from django.conf import settings


# Create your models here.
class Questionaire(models.Model):
    title = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title
