from django.db import models


# Create your models here.


class TestLoans(models.Model):
    STATUS = (
        ('1', 'One'),
        ('2', 'Two'),
        ('3', 'Three'),
    )
    choose = models.CharField(max_length=5, choices=STATUS)
    test_decimal = models.DecimalField(max_digits=14, decimal_places=4, null=True, blank=True)


class Loans(models.Model):
    current_balance = models.DecimalField(max_digits=14, decimal_places=4)
    original_balance = models.DecimalField(max_digits=14, decimal_places=4)
    interest_rate = models.FloatField()

    def __repr__(self):
        return str(self.current_balance)


