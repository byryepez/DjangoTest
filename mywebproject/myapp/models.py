from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Order(models.Model):
    PO_number = models.Charfield(max_length = 30)