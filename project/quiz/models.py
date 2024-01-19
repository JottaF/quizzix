from django.db import models
from django.contrib.auth.models import User
  
class Tag(models.Model):
  name = models.CharField(max_length=20)
  color = models.CharField(max_length=50)

  def __str__(self) -> str:
    return self.name

class Quiz(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=255)
  is_private = models.BooleanField(default=False)
  participants = models.JSONField(null=True, blank=True)
  start_date = models.DateTimeField()
  expiration_date = models.DateTimeField()
  created_at = models.DateTimeField(auto_now_add=True)
  tags = models.ManyToManyField(Tag)

  def __str__(self) -> str:
    return f"Id: {self.pk} | Title: {self.title} | Author: {self.author}"

class Question(models.Model):
  quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
  text = models.TextField(blank=True)
  image = models.ImageField(blank=True, null=True)

  def __str__(self) -> str:
    return f"Id: {self.pk} | Quiz: {self.quiz.pk} | Text: {self.text}"
  
class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  content = models.TextField(null=True)
  image_url = models.URLField(blank=True, null=True)

  def __str__(self) -> str:
    return f"Id: {self.pk} | Question: {self.question.pk} | Content: {self.content}"

class UserQuiz(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

  def __str__(self) -> str:
    return f"User: {self.user} | Quiz: {self.quiz.pk}"
  
class UserResponse(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
  response = models.JSONField()

  def __str__(self) -> str:
    return f"User: {self.user} | Quiz: {self.quiz.pk} | Response: {self.response}"