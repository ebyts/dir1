from django.shortcuts import render , HttpResponse , get_list_or_404
from cine.models import Product
from django.db.models import Q

# Create your views here.


def SearchResult(request):
    products=None
    query=None

    if 'q' in request.GET:
        query=request.GET.get('q')
        products=Product.objects.all().filter(Q(name__contains=query)| Q(description__contains=query))
    return render(request,'search.html',{'query':query ,'products':products})