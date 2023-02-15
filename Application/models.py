from django.db import models

class table(models.Model):
    title = models.CharField(max_length=500)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)



# Create your models here.
