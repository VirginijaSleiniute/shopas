from venv import create
from .models import Category, Item, OrderLine, Designer, Cart
from django.core.paginator import Paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):
    num_items = Item.objects.all().count()
    num_designers = Designer.objects.all().count()

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_items': num_items,
        'num_designers': num_designers,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)


def designers(request):
    paginator = Paginator(Designer.objects.all(), 2)
    page_number = request.GET.get('page')
    paged_designers = paginator.get_page(page_number)
    context = {
        'designers': paged_designers
    }
    return render(request, 'designers.html', context=context)


def designer(request, designer_id):
    single_designer = get_object_or_404(Designer, pk=designer_id)
    return render(request, 'designer.html', context={"designer": single_designer})


def search(request):
    query = request.GET.get('query')
    search_results = Item.objects.filter(Q(title__icontains=query) | Q(summary__icontains=query))
    context = {
        "query": query,
        "items": search_results,
    }
    return render(request, "results.html", context=context)


class ItemListView(generic.ListView):
    model = Item
    paginate_by = 6
    template_name = 'item_list.html'
    context_object_name = 'items'
    

class ItemDetailView(generic.DetailView):
    model = Item
    template_name = 'item_detail.html'
    context_object_name = 'item'


@login_required
def cart(request):
    try:
        cart = Cart.objects.get(user = request.user, status='k')
    except:
        cart = Cart(user = request.user, status='k')
        cart.save()
    context = {'cart':cart}
    return render(request, 'cart.html', context)


@login_required
def add_to_cart(request, item_id, qty):
    item = Item.objects.get(pk=item_id)
    try:
        cart = Cart.objects.get(user = request.user, status='k')
    except:
        cart = Cart(user = request.user, status='k')
        cart.save()
  
    order_line = OrderLine(item=item, cart=cart, qty=qty)
    order_line.save()
    
    context = {'cart':cart}
    return render(request, 'cart.html', context)








