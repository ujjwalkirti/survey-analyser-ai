from django import forms


class QuestionaireForm(forms.Form):
    questionaire_title = forms.CharField(max_length=200, label="Questionaire Title")
    questionaire_description = forms.Textarea()
    questionaire_published_status = forms.BooleanField(
        label="Do you want to publish the questionaire?", required=False
    )
