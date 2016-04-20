from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField("published time")
    author = models.CharField(max_length = 50)
    content = models.TextField(blank = True, null = True)


    def __str__(self):
        return self.title
