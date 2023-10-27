from django.db import models

class addbook(models.model):
    author=models.CharField(max_length=200,null=False,blank=False)
    title=models.CharField(max_length=200,null=False,blank=False)
    cost=models.CharField(max_length=200,null=False,blank=False)

def __str__(self):
    return self.title