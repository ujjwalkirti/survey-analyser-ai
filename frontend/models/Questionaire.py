from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Questionaire(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    description = models.TextField(null=True)
    pub_date = models.DateTimeField("date published", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def save(self, *args, **kwargs):
        if self.is_published:
            self.pub_date = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
