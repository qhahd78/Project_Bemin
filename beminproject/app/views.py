from django.shortcuts import render, redirect
from .models import Item

# Create your views here.

def home(request):
    # shop = Item.objects.all()
    # return render(request, 'home.html', {'shop':shop})
    return render (request, 'home.html',)

def create(request):
    if request.method == 'POST':
        item = Item() 
        item.name = request.POST['name']
        item.price = request.POST['price']
        item.save()
        return redirect('home') 

def update(request, item_id):
    # 강의를 따라 완성해봅시다.
    pass

def delete(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.delete()
    return redirect('home')

