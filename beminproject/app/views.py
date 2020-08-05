from django.shortcuts import render

# Create your views here.

def order(request):
    return render(request, 'order.html')

def order_list(request):
    return render(request, 'order_list.html')

def order_update(request):
    return render(request, 'order_update.html')

