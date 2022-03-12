from tkinter import CASCADE
from django.db import models
from more_itertools import quantify

# Create your models here.


class Order(models.Model):
    PO_number = models.CharField(max_length = 30)

class Item(models.Model):
    Order = models.ForeignKey(Order, on_delete=CASCADE)
    quantity = models.IntegerField()
    value = models.DecimalField()
    