from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Order, Store

# Create your views here.

def home(request):
    # shop = Item.objects.all()
    # return render(request, 'home.html', {'shop':shop})
    return render (request, 'home.html',)

def order(request):
    if request.method == 'POST':
        item = Order() 
        item.store = request.POST['store']
        item.menu = request.POST['menu']
        item.side = request.POST['side']
        item.address = request.POST['address']
        item.save()
        return redirect('order_list') 
    else :
        return render (request, 'order.html', )

def update(request, item_id):
    item = get_object_or_404(Order, pk=item_id)
    if request.method == 'POST':
        item.store = request.POST['store']
        item.menu = request.POST['menu']
        item.side = request.POST['side']
        item.adrress = request.POST['address']
        item.save()
        return redirect('home')
    else :
        return render (request, 'update.html', {'Items':item})

def delete(request, item_id):
    item = get_object_or_404(Order, pk=item_id)
    item.delete()
    return redirect('home')

def order_list(request):
    order = Order.objects.all()
    return render (request, 'order_list.html',{'order':order})

def store(request):
    store = Store.objects.all()
    return render (request, 'store.html',{'store':store})


