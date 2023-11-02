from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    steps = models.TextField()
    cooking_time = models.IntegerField()
    image = models.ImageField(upload_to='recipes/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    recipe_count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user.username