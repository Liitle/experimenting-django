import django_tables2 as tables

from dashboard.models import Expenses


class ExpensesTable(tables.Table):
    class Meta:
        model = Expenses
        attrs = {'class': 'table'}
