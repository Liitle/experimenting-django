from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Expenses


def index(request):
    all_expenses = Expenses.objects.all()
    template = loader.get_template('dashboard/dashboard.html')
    context = {
        'all_expenses': all_expenses,
    }
    return render(request, 'dashboard/dashboard.html', context)


def detail(request, expense_id):
    return HttpResponse("<h2>Expense details  " + str(expense_id) + " </h2>")
