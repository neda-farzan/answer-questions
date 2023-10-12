from django.contrib.admin.templatetags.admin_list import search_form
from django.shortcuts import render, get_object_or_404
from give_ansewr_question.models import Question
from .forms import AnswerForm, AskForm, SearchForm


def question_list(request):
    questions = Question.objects.all()
    return render(request, 'list.html', {'questions': questions})


def question_detail(request, year, month, day, question):
    question = get_object_or_404(Question, create__year=year,
                                 create__month=month, create__day=day, slug=question)

    answers = question.answers.all()
    new_answer = None
    if request.method == 'POST':
        answer_form = AnswerForm(data=request.POST)
        if answer_form.is_valid():
            # new_answer = answer_form.save()
            new_answer = answer_form.save(commit=False)
            new_answer.question = question
            new_answer.save()

    else:
        answer_form = AnswerForm()

    return render(request, 'detail.html', {'question': question, 'answers': answers,
                                           'answer_form': answer_form, 'new_answer': new_answer})


def new_question(request):
    new = False
    ask_form = None
    empty_form = None
    if request.method == 'POST':
        ask_form = AskForm(data=request.POST)
        if ask_form.is_valid():
            ask_form.save()
            new = True
    else:
        empty_form = AskForm()
    return render(request, 'ask.html', {'ask_form': ask_form, 'empty_form': empty_form, 'new': new})


def index(request):
    return render(request, 'index.html')


def question_search(request):
    form = SearchForm()
    results = []
    query = None
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Question.objects.filter(title__contains='query')
    return render(request, 'search.html', {'form': form, 'query': query, 'results': results})
