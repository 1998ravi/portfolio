from django.db import models

# Create your models here.
class pr(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField()
    Tech=models.CharField(max_length=100)
    image=models.ImageField(upload_to="img/")
    li=models.CharField(max_length=100,null=True)

    def __str__(self) -> str:
        return self.name

class c(models.Model):
    n=models.CharField(max_length=100)
    e=models.EmailField()
    com=models.CharField(max_length=100)
     
    def __str__(self) -> str:
        return self.com
            