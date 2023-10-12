from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Question(models.Model):
    title = models.CharField(max_length=250, null=False, blank=False)
    slug = models.CharField(max_length=250)
    subject = models.CharField(max_length=250, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('questions:question_detail',
                       args=[self.create.year,
                             self.create.month,
                             self.create.day,
                             self.slug]
                       )


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    name = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    body = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    efficient = models.BooleanField(default=True)

    def __str__(self):
        return f'answer by {self.name} on {self.question.title}'


