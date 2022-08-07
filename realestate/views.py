from django.shortcuts import render,redirect ,get_object_or_404
from django.db.models import Q
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
from realestate.models import Product,Agent ,Comment ,Type , City , Region ,Room , Category , Images


def index(request):
    categorys = Category.objects.all()
    types = Type.objects.all()
    citys = City.objects.all()
    regions = Region.objects.all()
    rooms = Room.objects.all()
    comments = Comment.objects.all()
    agents = Agent.objects.all()
    opportunitys = Product.objects.filter(opportunity=True)
    sliders = Product.objects.filter(slider=True)
    products = Product.objects.filter(available=True)


    sender = Category.objects.all()
    saleminilistnavbar = Product.objects.filter(type__name__icontains='Satılık')
    rentminilistnavbar = Product.objects.filter(type__name__icontains='Kiralık')


    context = {
        'categorys':categorys,
        'sliders':sliders,
        'products':products,
        'opportunitys':opportunitys,
        'saleminilistnavbar':saleminilistnavbar,
        'rentminilistnavbar':rentminilistnavbar,
        'agents':agents,
        'comments':comments,
        'types':types,
        'citys':citys,
        'regions':regions,
        'rooms':rooms,
        'sender':sender
    }
    return render(request,'central/index.html',context)

def about(request):
    sender = Category.objects.all()
    saleminilistnavbar = Product.objects.filter(type__name__icontains='Satılık')
    rentminilistnavbar = Product.objects.filter(type__name__icontains='Kiralık')


    context = {
        'sender':sender,
        'saleminilistnavbar':saleminilistnavbar,
        'rentminilistnavbar':rentminilistnavbar
    }

    return render(request,'central/about.html',context)

def product_list(request):
    sliders = Product.objects.filter(slider=True)


    sender = Category.objects.all()
    saleminilistnavbar = Product.objects.filter(type__name__icontains='Satılık')
    rentminilistnavbar = Product.objects.filter(type__name__icontains='Kiralık')
    products = Product.objects.all()



    context = {
        'products':products,
        'sliders':sliders,
        'sender':sender,
        'saleminilistnavbar':saleminilistnavbar,
        'rentminilistnavbar':rentminilistnavbar
    }

    return render(request,'central/list.html',context)



def product_sale(request,category_slug = None):
    sender = Category.objects.all()
    saleminilistnavbar = Product.objects.filter(type__name__icontains='Satılık')
    rentminilistnavbar = Product.objects.filter(type__name__icontains='Kiralık')
    categorys = Category.objects.all()
    citys = City.objects.all()
    products = Product.objects.filter(type__name__icontains='Satılık').order_by('-id')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'category': category,
        'products': products,
        'categorys': categorys,
        'citys': citys,
        'sender':sender,
        'saleminilistnavbar':saleminilistnavbar,
        'rentminilistnavbar':rentminilistnavbar
    }

    return render(request,'central/salelist.html',context)



def product_rent(request,category_slug = None):
    sender = Category.objects.all()
    saleminilistnavbar = Product.objects.filter(type__name__icontains='Satılık')
    rentminilistnavbar = Product.objects.filter(type__name__icontains='Kiralık')
    categorys = Category.objects.all()
    citys = City.objects.all()
    products = Product.objects.filter(type__name__icontains='Kiralık').order_by('-id')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'category': category,
        'products': products,
        'categorys': categorys,
        'citys': citys,
        'sender':sender,
        'saleminilistnavbar':saleminilistnavbar,
        'rentminilistnavbar':rentminilistnavbar
    }

    return render(request,'central/salelist.html',context)

def product_detail(request,slug,id):
    if 'btnSubmit' in request.POST:
        if True:
            nerden= 'Taşhan Emlak iletişim formu mesajı-Central Web Agency'
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            messages = request.POST.get('messages')

            subject = 'Contact Page Costumer Back'
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email,"djangomarmaris@gmail.com","info@tashanemlakinsaat.com"]
            contact_message = "\nNerden:%s\nName:%s\nEmail:%s\nPhone:%s\nMessages:%s" % (
                nerden,
                name,
                email,
            phone,
            messages)
            send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
        return redirect('/')
    sender = Category.objects.all()
    saleminilistnavbar = Product.objects.filter(type__name__icontains='Satılık')
    rentminilistnavbar = Product.objects.filter(type__name__icontains='Kiralık')
    product = get_object_or_404(Product, slug=slug,id=id, available=True)
    images = Images.objects.filter(product_id = id)



    context = {
       'sender':sender ,
        'saleminilistnavbar':saleminilistnavbar,
        'rentminilistnavbar':rentminilistnavbar,
        'product':product,
        'images':images
    }


    return render(request,'central/detail.html',context)



def filter(request):
    sender = Category.objects.all()
    saleminilistnavbar = Product.objects.filter(type__name__icontains='Satılık')
    rentminilistnavbar = Product.objects.filter(type__name__icontains='Kiralık')


    city = request.GET.get('city')
    print('''''City''',city)
    region = request.GET.get('region')
    print('''''region''', region)
    type = request.GET.get('type')
    print('''''type''', type)
    model = request.GET.get('model')
    print('''''model''', model)
    minArea = request.GET.get('min')
    print('''''City''', city)
    price = request.GET.get('price')
    #maxArea = request.GET.get('max')
    print('wow',price)


    products = Product.objects.filter(Q(m2__gte='75') & Q(price__gte='800000') & Q(city__name__contains=city)  &  Q(region__name__icontains=region) & Q(type__name__icontains=type) & Q(category__name__icontains=model))

    return render(request,'central/filter.html',{'products':products,'sender':sender,'saleminilistnavbar':saleminilistnavbar,'rentminilistnavbar':rentminilistnavbar})



def contact(request):
    sender = Category.objects.all()
    saleminilistnavbar = Product.objects.filter(type__name__icontains='Satılık')
    rentminilistnavbar = Product.objects.filter(type__name__icontains='Kiralık')
    if 'btnSubmit' in request.POST:
        if True:
            nerden= 'Taşhan Emlak iletişim formu mesajı-Central Web Agency'
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            messages = request.POST.get('messages')

            subject = 'Contact Page Costumer Back'
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email,"djangomarmaris@gmail.com","info@tashanemlakinsaat.com"]
            contact_message = "\nNerden:%s\nName:%s\nEmail:%s\nPhone:%s\nMessages:%s" % (
                nerden,
                name,
                email,
            phone,
            messages)
            send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
        return redirect('/')
    context = {
        'sender':sender,
        'saleminilistnavbar':saleminilistnavbar,
        'rentminilistnavbar':rentminilistnavbar
    }
    return render(request,'central/contact.html',context)