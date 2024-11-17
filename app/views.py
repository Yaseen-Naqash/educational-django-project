from django.shortcuts import render
from .models import Manufacturer, Mobile


def home(request):


    query = request.GET.get('q', '')  # Get the search query from the URL

    mobiles = Mobile.objects.all()

    if query:
        mobiles = mobiles.filter(title__icontains=query)

    context = {
        'mobiles' : mobiles,
    }

    return render (request, 'index.html', context)  
# Create your views here.
