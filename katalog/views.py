from django.shortcuts import render
from katalog.models import CatalogItem

def show_katalog(request):
    data_katalog_item = CatalogItem.objects.all()
    context = {
        'list_item' : data_katalog_item,
        'name' : "Nicholas Lexi",
        'id' : "2106720960",
    }
    return render(request, "katalog.html", context)
# TODO: Create your views here.
