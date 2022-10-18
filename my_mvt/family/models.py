from django.db import models
from django.forms import DateInput


class family(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    ages = models.IntegerField()
    relation = models.CharField(max_length=40)
    birth_year = models.DateField()
   
    def __str__(self):
        return f"Name: {self.name} | Last_name: {self.last_name} | Age: {self.ages} | Relation: {self.relation} | birth_year: {self.birth_year}"
