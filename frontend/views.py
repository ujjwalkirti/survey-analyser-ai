from django.shortcuts import redirect, render
from frontend.forms import QuestionaireForm
from frontend.models.Questionaire import Questionaire
from django.http import HttpResponseRedirect

from frontend.models.Question import Question
from django.contrib.auth.decorators import login_required


# Create your views here.
# @login_required()
def home_page(request):
    # questionaires = request.user.questionaire_set.all()
    questionaires = Questionaire.objects.all()
    return render(
        request,
        "index/home.html",
        context={
            "title": "Welcome to Survey AI analyser!",
            "questionaires": questionaires,
        },
    )


# @login_required()
def questionaire_page(request, questionaire_id):
    questionaire = Questionaire.objects.get(id=questionaire_id)
    questions = Question.objects.filter(questionaire=questionaire)
    return render(
        request,
        "index/questionaire.html",
        context={"questions": questions, "questionaire": questionaire},
    )


def login_page(request):
    return render(request, "login.html")


# @login_required()
def create_questionaire(request):
    if request.method == "POST":
        form = QuestionaireForm(request.POST)
        if form.is_valid():
            questionaire = form.save(commit=False)
            questionaire.user = request.user
            questionaire.save()
            return HttpResponseRedirect("/")
    else:
        form = QuestionaireForm()

    return render(request, "index/create_questionaire.html", {"form": form})
