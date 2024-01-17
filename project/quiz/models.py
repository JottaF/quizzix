from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
  author_id = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=255)
  is_private = models.BooleanField(default=False)
  participants = models.JSONField(null=True, blank=True)
  start_date = models.DateTimeField()
  expiration_date = models.DateTimeField()
  created_at = models.DateTimeField(auto_now_add=True)

class Question(models.Model):
  quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
  text = models.TextField(blank=True)
  image = models.ImageField(blank=True, null=True)
  
class UserQuiz(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
  
class UserResponse(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
  response = models.JSONField()