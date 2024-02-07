from django import forms

from frontend.models.Questionaire import Questionaire


class QuestionaireForm(forms.ModelForm):
    class Meta:
        model = Questionaire
        fields = ["title", "author", "is_published", "description"]
        labels = {
            "title": "Questionaire Title",
            "author": "Author",
            "is_published": "Do you want to publish the questionaire?",
            "description": "Questionaire Description",
        }
