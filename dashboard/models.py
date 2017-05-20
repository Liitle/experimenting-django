from django.db import models


class Expenses(models.Model):
    expense_name = models.CharField(max_length=250)
    value = models.IntegerField()
    currency = models.CharField(max_length=10)
    category = models.CharField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return '{} {}'.format(self.expense_name, self.value)
