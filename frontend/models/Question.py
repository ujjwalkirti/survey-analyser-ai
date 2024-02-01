from django.db import models

from frontend.models.Questionaire import Questionaire


class Question(models.Model):
    question = models.TextField()
    isMCQ = models.BooleanField(default=True)
    questionaire = models.ForeignKey(Questionaire, on_delete=models.CASCADE)

    def __str__(self):
        return self.question
