from django.db import models

# Create your models here.

PRIORITY = (('danger','high'),('warning','medium'),('success','low')) 
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length = 50,
        choices = PRIORITY
    )
    duedatetime = models.DateTimeField()
    def __str__(self):
        return self.title