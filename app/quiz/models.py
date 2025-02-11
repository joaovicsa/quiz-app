from django.db import models
from django.contrib.auth.models import AbstractUser


# Tipos de Usuários
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_player = models.BooleanField(default=True)


# Categorias do Quiz
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# Quiz com categorias
class Quiz(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Quiz {self.id} - {self.category.name}"


# Perguntas do Quiz
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text


# Respostas do Quiz
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


# Pontuação dos jogadores
class PlayerScore(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    score = models.IntegerField(default=0)