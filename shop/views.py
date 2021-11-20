import json
from django.shortcuts import render
from django.http import HttpResponse
# to use any model i need to import it from models.py file as shown below:
from .models import Product, Feedback, Order, OrderUpdate
from math import ceil
from django.utils import timezone

# Create your views here.


def index(request):

    # each item(dict) in products list will have category&id fields
    # list of dicts
    products = Product.objects.values('category', 'id')
    # list be like: products = [ 0[category_0,id_0] , 1[category_1,id_1] , 2[category_2,id_2] ]

    # set of unique categories of Product Model
    categories = {item['category'] for item in products}

    # allProds will contain all the required list i.e. categorywise lists
    allProds = []

    for category in categories:
        # list of all the objects of given category
        prods = Product.objects.filter(category=category)
        n = len(prods)
        # to calculate total no. of slides using n
        # //_Floor division & /_Normal division
        slides = n//4 + ceil(n/4 - n//4)
        # appending a list of same category products
        allProds.append([prods, range(1, slides)])

    # final allProds be like:
    # allProds = [ 0[prods,range] , 1[prods,range] , 2[prods,range] ......]

    params = {
        'allProds': allProds
    }

    return render(request, 'shop/home.html', params)


def about(request):
    return render(request, 'shop/about.html')


def support(request):
    if request.method == "POST":
        # customer_id = request.POST.get('customer_id','no_id')
        name = request.POST.get('name', 'default')
        email = request.POST.get('email', 'default')
        phone = request.POST.get('phone', '0')
        desc = request.POST.get('desc', 'default')
        date = timezone.now()
        print(name, email, phone, desc)
        # creating Feedback obj & storing all data in it
        # this obj will also be appearing in django-admin
        feedback = Feedback(name=name, email=email,
                            phone=phone, desc=desc, date=date)
        # saving the obj to models/django-admin
        feedback.save()
    return render(request, 'shop/support.html')


def search(request):
    search = request.GET.get('search', '')
    if search == '':
        return index(request)
    else:
        search = search.lower()
        products = Product.objects.values('category')
        categories = set()
        for item in products:
            categories.add(item['category'])
        prods = []
        allProds = []
        for cat in categories:
            products = Product.objects.filter(category=cat)
            for product in products:
                if search in product.product_name.lower() or search in product.category.lower() or search in product.desc.lower():
                    prods.append(product)
            total = len(prods)
            slides = total//4 + ceil(total/4 - total//4)
            if prods != []:
                allProds.append([prods, range(1, slides)])
            prods = []

        params = {
            'allProds': allProds,
        }
        return render(request, 'shop/search.html', params)


def product(request, myid):
    product = Product.objects.filter(id=myid)
    # print(product[0])
    param = {
        'product': product[0]
    }
    return render(request, 'shop/product.html', param)


def tracker(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        order_id = request.POST.get('order_id',)
        try:
            # check if an Order of entered details is really registered or not
            order = Order.objects.filter(email=email, order_id=order_id)
            print(order)
            # if yes then order will have some value & not be null
            if len(order) > 0:
                # get all the OrderUpdate entries with same order_id
                update = OrderUpdate.objects.filter(order_id=order_id)
                updates = []
                for item in update:
                    # take only the details to be displayed
                    updates.append(
                        {'update': item.update_desc, 'time': item.timestamp})
                    print(updates)
                    # dump as json obj
                    response = json.dumps(
                        [updates, order[0].itemsJSON], default=str)
                return HttpResponse(response)
            else:
                print('else')
                return HttpResponse({})
        except Exception as e:
            # this will occur if there is no Order with entered details
            print('exceptions is : '+e)
            return HttpResponse({})
    return render(request, 'shop/tracker.html')


def checkout(request):
    if request.method == 'POST':
        itemsJSON = request.POST.get('itemsJSON', '')
        amount = request.POST.get('amount', '')
        firstname = request.POST.get('firstname', '')
        lastname = request.POST.get('lastname', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        order = Order(itemsJSON=itemsJSON, amount=amount, firstname=firstname, lastname=lastname,
                      email=email, phone=phone, address=address, city=city, state=state, zip_code=zip_code)
        order.save()
        flag = True
        # getting id of newly generated order obj
        id = order.order_id
        params = {
            'id': id,
            'flag': flag
        }
        update = OrderUpdate(
            order_id=id, update_desc="Hurray!Order has been placed")
        update.save()
        return render(request, 'shop/checkout.html', params)
    return render(request, 'shop/checkout.html')
