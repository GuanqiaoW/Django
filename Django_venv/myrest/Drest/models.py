from django.db import models


class Person(models.Model):
  firstname = models.CharField(max_length=200)
  lastname= models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

  def __str__(self):
    return self.firstname


