from django.db import models

# Create your models here.
class Text(models.Model):
    text = models.CharField(max_length=200)
    pub_text = models.DateTimeField('Activation date')

class Choice(models.Model):
    text = models.ForeignKey(Text, on_delete=models.CASCADE)
    Choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


    
