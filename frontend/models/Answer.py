
from django.db import models

from frontend.models.Question import Question

class Answer(models.Model):
    answer_text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer_text
