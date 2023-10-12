from django.urls import path
from . import views

app_name = 'questions'

urlpatterns = [
    path('', views.index, name='index'),
    path("questions/", views.question_list, name="question_list"),
    path("<int:year>/<int:month>/<int:day>/<slug:question>/",
         views.question_detail, name='question_detail'),
    path("ask/", views.new_question, name='new_question'),
    path("search/", views.question_search, name='question_search')
]
