from django.shortcuts import render, redirect
from .models import Stock, Customer, Order, OrderItems
from .forms import StockCreateForm, StockSearchForm, StockUpdateForm, CustomerCreateForm, CustomerSearchForm, CustomerUpdateForm, OrderCreateForm, OrderSearchForm, OrderUpdateForm, OrderItemsCreateForm, OrderItemsSearchForm, OrderItemsUpdateForm
from .filters import StockFilter

def home(request):
    title = "Welcome to PDGames HomePage"
    context = {
        "title" :  title,
    }
    return render(request, "base.html",context)


def list_item(request):
    title = "List OF Game Titles"
    form = StockSearchForm(request.POST or None)
    queryset = Stock.objects.all()
    if request.method == "POST":
        queryset = Stock.objects.filter(game_title__icontains=form['game_title'].value())
    context = {
        "title" : title,
        "queryset" : queryset,
        "form" : form
    }
    return render(request, "list_item.html", context)

def add_items(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/list_item')
    context = {
        "form" : form,
        "title": "Page To add Item"
    }
    return render(request, "add_items.html", context)


def search(request):
    stock_list = Stock.objects.all()
    stock_filter = StockFilter(request.GET, queryset=stock_list)
    return render(request, 'search/mylist.html', {'filter': stock_filter})

def update_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = StockUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = StockUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/list_item')
    context = {
        'form' : form
    } 

    return render(request, 'add_items.html', context)

def delete_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    if request.method == "POST":
        queryset.delete()
        return redirect('/list_item')
    return render(request, 'delete_items.html')

def stock_detail(request, pk):
    queryset = Stock.objects.get(id=pk)
    context = {
        "title" : queryset.game_title,
        "queryset": queryset
    }
    return render(request, "stock_detail.html", context)

def add_customer(request):
    form = CustomerCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/list_customer')
    context = {
    "form" : form,
    "title": "Page To add Customer"
    }

    return render(request, "add_customer.html", context)


def list_customer(request):
    title = "Customer Information"
    form = CustomerSearchForm(request.POST or None)
    queryset = Customer.objects.all()
    if request.method == "POST":
        queryset = Customer.objects.filter(first_name__icontains=form['first_name'].value())
    context = {
        "title" : title,
        "queryset" : queryset,
        "form" : form
    }
    #print(context)
    return render(request, "list_customer.html", context)

def update_customer(request, pk):
    queryset = Customer.objects.get(id=pk)
    form = CustomerUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = CustomerUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/list_customer')
    context = {
        'form' : form
    } 

    return render(request, 'add_customer.html', context)


def delete_customer(request, pk):
    queryset = Customer.objects.get(id=pk)
    if request.method == "POST":
        queryset.delete()
        return redirect('/list_customer')
    return render(request, 'delete_customer.html')


def customer_detail(request, pk):
    queryset = Customer.objects.get(id=pk)
    context = {
        "title" : queryset.first_name,
        "queryset": queryset
    }
    return render(request, "customer_detail.html", context)
# Create your views here.


def add_order(request):
    form = OrderCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/list_order')
    context = {
        "form" : form,
        "title": "Page To add Item"
    }
    return render(request, "add_order.html", context)


def list_order(request):
    title = "List OF Orders"
    form = OrderSearchForm(request.POST or None)
    queryset = Order.objects.all()
    if request.method == "POST":
        queryset = Order.objects.filter(customer__icontains=form['customer'].value())
    context = {
        "title" : title,
        "queryset" : queryset,
        "form" : form
    }
    #print(context)
    return render(request, "list_order.html", context)

def update_order(request, pk):
    queryset = Order.objects.get(id=pk)
    form = OrderUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = OrderUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/list_order')
    context = {
        'form' : form
    } 

    return render(request, 'add_order.html', context)

def delete_order(request, pk):
    queryset = Order.objects.get(id=pk)
    if request.method == "POST":
        queryset.delete()
        return redirect('/list_order')
    return render(request, 'delete_order.html')

def order_detail(request, pk):
    queryset = Order.objects.get(id=pk)
    context = {
        "title" : queryset.customer,
        "queryset": queryset
    }
    return render(request, "order_detail.html", context)

def add_orderitems(request):
    form = OrderItemsCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/list_orderitems')
    context = {
    "form" : form,
    "title": "Page To add OrderItems"
    }

    return render(request, "add_orderitems.html", context)

def list_orderitems(request):
    title = "List OF Order Items"
    form = OrderItemsSearchForm(request.POST or None)
    queryset = OrderItems.objects.all()
    if request.method == "POST":
        queryset = OrderItems.objects.filter(customer__icontains=form['order'].value())
    context = {
        "title" : title,
        "queryset" : queryset,
        "form" : form
    }
    #print(context)
    return render(request, "list_orderitems.html", context)



def update_orderitems(request, pk):
    queryset = OrderItems.objects.get(id=pk)
    form = OrderItemsUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = OrderItemsUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/list_orderitems')
    context = {
        'form' : form
    } 

    return render(request, 'add_orderitems.html', context)



def delete_orderitems(request, pk):
    queryset = OrderItems.objects.get(id=pk)
    if request.method == "POST":
        queryset.delete()
        return redirect('/list_orderitems')
    return render(request, 'delete_orderitems.html')


def orderitems_detail(request, pk):
    queryset = OrderItems.objects.get(id=pk)
    context = {
        "title" : queryset.order,
        "queryset": queryset
    }
    return render(request, "orderitems_detail.html", context)
