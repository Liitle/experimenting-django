from django.http import HttpResponse
from django.shortcuts import render

from dashboard.tables import ExpensesTable
from .models import Expenses


def index(request):
    all_expenses = Expenses.objects.all()
    table = ExpensesTable(all_expenses)
    return render(request, 'dashboard/dashboard.html', {"table": table})


def detail(request, expense_id):
    return HttpResponse("<h2>Expense details  " + str(expense_id) + " </h2>")
