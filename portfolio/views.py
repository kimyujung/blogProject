from django.shortcuts import render, redirect
from .models import Portfolio
# Create your views here.
def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio.html', {'portfolios' : portfolios})
def newphoto(request):
    return render(request, 'newphoto.html')
