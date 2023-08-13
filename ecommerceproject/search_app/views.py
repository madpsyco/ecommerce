from django.shortcuts import render
from ecommerceapp.models import Product
from django.db.models import Q
# Create your views here.

def SearchResult(request):
    products=None
    querry=None
    if 'q' in request.GET:
        querry=request.GET.get('q')
        products=Product.objects.all().filter(Q(name__icontains=querry) | Q(description__icontains=querry))

        return render(request,'search.html',{'querry':querry,'products':products})

