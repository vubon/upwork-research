from django.db import models

# Create your models here.
from loans_app.models import Loans


class Offer(models.Model):
    loan = models.ForeignKey(Loans)
    title = models.CharField(max_length=100)