from django.shortcuts import render

# Create your views here.

def home(request):
    """
    Render the home page of the portfolio.
    """
    return render(request, 'portfolio/index.html')