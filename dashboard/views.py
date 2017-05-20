from django.http import HttpResponse
from .models import Expenses


def index(request):

    all_expenses = Expenses.objects.all()
    html = ''
    for expense in all_expenses:
        url = '/dashboard/{expense_id}/'.format(expense_id=expense.id)
        html += '<a href="{url}">{expense_name}</a></br>'.format(url=url, expense_name=expense.expense_name)
    return HttpResponse(html)


def detail(request, expense_id):
    return HttpResponse("<h2>Expense details  " + str(expense_id) + " </h2>")
