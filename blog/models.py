from django.db import models

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        s = self.body[0:50]
        return s


    def __str__(self):
        return self.title