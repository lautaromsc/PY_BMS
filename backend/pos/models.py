from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Employee(models.Model):
        fullname = models.CharField(null=True, max_length=100)
        emp_code = models.CharField(null=True, max_length=3)
        mobile = models.CharField(null=True, max_length=15)

