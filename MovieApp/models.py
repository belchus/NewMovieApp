from django.db import models
from django.contrib.auth.models import User as UserAuth
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ValidationError


class User(models.Model):
    user = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    rol= models.CharField(max_length=40)
    email = models.EmailField()
    avatar = models.CharField(max_length= 250)


    
class Movie(models.Model):
    title =  models.CharField(max_length=40)
    img =  models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=500)
    tag = models.CharField(max_length=40)

def validate_score(value):
    if value < 1 or value > 5:
        raise ValidationError('El puntaje debe estar entre 1 y 5.')
    
    
class Review(models.Model):
    title =  models.CharField(max_length=40)
    text = models.CharField(max_length=500)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user =models.ForeignKey(UserAuth,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    rated = models.IntegerField(default=1, validators=[validate_score])

    def __srt__(self):
        return f'Review de MovieUser: {self.user}'

class Avatar(models.Model):
    user = models.OneToOneField(UserAuth, on_delete= models.CASCADE)
    image = models.ImageField(upload_to='avatars', null=True, blank=True)

    def __srt__(self):
        return self.user.user
    
class Reply(models.Model):
    title =  models.CharField(max_length=40)
    text = models.CharField(max_length=500)
    user =models.ForeignKey(UserAuth,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    review =models.ForeignKey(Review,on_delete=models.CASCADE, null=True)

def __str__(self):
        return f'Reply de MovieUser: {self.user}'

