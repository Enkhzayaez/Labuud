from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    item_list = Item.objects.all()
    category_list = Category.objects.all()
    item_dic = {'items': item_list,
                'categories': category_list }
    return render(request, 'index.html', context = item_dic)

def page(request):
    item_list = Item.objects.all()
    p = Paginator(item_list, 9)
    page_number = request.GET.get("page")
    page_obj = p.get_page(page_number)
    category_list = Category.objects.all()
    item_dic = {'items': item_list,
                'categories': category_list,
                "page_obj": page_obj}
    return render(request, "page.html",context=item_dic)