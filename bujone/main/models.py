from django.db import models
from django.contrib.auth.models import User
from django.conf import settings



# Create your models here.


    
    
    

class JournalModel(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    desc = models.TextField(max_length=400, null=True, blank=True)
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

#one bujoneuser has many journals
#we need to save the journals of the user (journal1,journal2)


class Todo(models.Model):
    text = models.CharField(max_length=40, null=True, blank=True)
    complete = models.BooleanField(default=False)
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.text

#we need to save the todo's for the todolist

class Idea(models.Model):
    text = models.CharField(max_length=100, null=True, blank=True)
    complete = models.BooleanField(default=False)
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text

#we need to save the ideas








