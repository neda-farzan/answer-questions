from django.contrib import admin
from .models import Question, Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'slug', 'create')
    list_filter = ('subject', 'create')
    search_fields = ('title', 'subject', 'description')
    date_hierarchy = 'create'
    prepopulated_fields = {"slug": ["title", ]}


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'body')
    list_filter = ('create', 'efficient')
    search_fields = ('body', 'email', 'name')
