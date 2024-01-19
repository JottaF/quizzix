from django.contrib import admin
from .models import Question, Quiz, Tag, UserQuiz, UserResponse, Choice

admin.site.register(Tag)
admin.site.register(Choice)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(UserQuiz)
admin.site.register(UserResponse)
