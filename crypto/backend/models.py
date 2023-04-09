from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Добавляем дополнительные поля

    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    # Возвращает полное имя пользователя
    def get_full_name(self) -> str:
        return f'{self.first_name} {self.last_login}'
    
    # Возвращает краткое имя пользователя
    def get_short_name(self) -> str:
        return f'{self.username}'
    

class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.category}'

class Post(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=256, blank=False, null=False)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    public = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    

