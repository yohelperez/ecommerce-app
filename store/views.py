from django.shortcuts import render
from .models import * 

# Create your views here.

def store(request):
    products = Product.objects.all()
    context = {'products': products}        #its used to pass data that its going to be shown in template
    return render(request, 'store/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete= False) #tries to query the customer to attach the order, if does not exist it created it and attaches order
        items = order.orderitem_set.all()      #asigna los items de la orden a items
    else:
        #instructions when user is not logged in
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0} #shows 0 for cart total and cart items when user is not logged in
    
    context = {'items': items, 'order': order }
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete= False) #tries to query the customer to attach the order, if does not exist it created it and attaches order
        items = order.orderitem_set.all()      #asigna los items de la orden a items
    else:
        #instructions when user is not logged in
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0} #shows 0 for cart total and cart items when user is not logged in
    
    context = {'items': items, 'order': order }
    return render(request, 'store/checkout.html', context)