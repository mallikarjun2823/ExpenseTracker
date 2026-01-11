from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from expenses.models import Expense

@api_view(['GET'])
# @login_required
def expenses(request):
    return HttpResponse("List of expenses")
# Create your views here.
