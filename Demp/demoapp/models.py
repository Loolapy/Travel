from django.db import models

# Create your models here.



class team(models.Model):
    names=models.CharField(max_length=250)
    imgs=models.ImageField(upload_to='pics')
    disc=models.TextField()

    def __str__(self):
        return self.names
