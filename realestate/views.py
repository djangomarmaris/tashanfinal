from django.shortcuts import render,redirect ,get_object_or_404
from django.db.models import Q
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
from realestate.models import Product, Agent, Comment, Type, City, Region, Room, Category, Images, Works

from django import template

register = template.Library()


@register.filter
def replace_commas(string):
    return string.replace(',', '.')

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
    regions = Region.objects.all()
    types = Type.objects.all()
    products = Product.objects.filter(type__name__icontains='Satılık').order_by('-id')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'category': category,
        'products': products,
        'categorys': categorys,
        'regions':regions,
        'types':types,
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
    regions = Region.objects.all()
    types = Type.objects.all()
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
        'regions':regions,
        'types':types,
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

            messages = request.POST.get('messages')

            subject = 'Contact Page Costumer Back'
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email,"djangomarmaris@gmail.com","info@tashanemlakinsaat.com"]
            contact_message = "\nNerden:%s\nName:%s\nEmail:%s\nMessages:%s" % (
                nerden,
                name,
                email,
            messages)
            send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
        return redirect('/')
    sender = Category.objects.all()
    saleminilistnavbar = Product.objects.filter(type__name__icontains='Satılık')
    rentminilistnavbar = Product.objects.filter(type__name__icontains='Kiralık')
    smiller = Product.objects.all().order_by('?')
    product = get_object_or_404(Product, slug=slug,id=id, available=True)
    images = Images.objects.filter(product_id = id)



    x = product.location.latitude
    print('XXXXX',x)
    y = product.location.longitude
    print('YYYYY',y)

    context = {
       'sender':sender ,
        'saleminilistnavbar':saleminilistnavbar,
        'rentminilistnavbar':rentminilistnavbar,
        'product':product,
        'images':images,
        'smiller':smiller,



    }


    return render(request,'central/detail.html',context)



def filter(request):
    sender = Category.objects.all()
    saleminilistnavbar = Product.objects.filter(type__name__icontains='Satılık')
    rentminilistnavbar = Product.objects.filter(type__name__icontains='Kiralık')
    categorys = Category.objects.all()
    types = Type.objects.all()
    citys = City.objects.all()
    regions = Region.objects.all()
    rooms = Room.objects.all()

    city = request.GET.get('city')
    print('''''City''',city)
    region = request.GET.get('region')
    print('''''region''', region)
    type = request.GET.get('type')
    print('''''type''', type)
    model = request.GET.get('model')




    products = Product.objects.filter(Q(city__name__contains=city)  &  Q(region__name__icontains=region) & Q(type__name__icontains=type) & Q(category__name__icontains=model))


    context = {'products':products,
               'sender':sender,
               'saleminilistnavbar':saleminilistnavbar,
               'rentminilistnavbar':rentminilistnavbar,
               'categorys':categorys,
               'types':types,
               'citys':citys,
               'regions':regions,
               'rooms':rooms}
    return render(request,'central/filter.html',context)

def price(request):
    sender = Category.objects.all()
    t1 = request.GET.get('t1', None)
    c1 = request.GET.get('c1', None)
    r1 = request.GET.get('render')

    print('T1',t1)
    print('C1', c1)
    print('R1', r1)



    if r1 == "LOW":
        if t1 == None:
            return redirect('/')
        else:
            products = Product.objects.filter(
                  Q(type__name__icontains=t1) & Q(
                    category__name__icontains=c1)).order_by('price')
    elif r1 =="HİGH":
        if c1 == None:
            return redirect('/')
        else:
            products = Product.objects.filter(
                Q(type__name__icontains=t1) & Q(
                    category__name__icontains=c1)).order_by('-price')
    context= {
        'products':products,
        'sender':sender,
    }

    return render(request,'central/price.html',context)

def contact(request):
    sender = Category.objects.all()
    saleminilistnavbar = Product.objects.filter(type__name__icontains='Satılık')
    rentminilistnavbar = Product.objects.filter(type__name__icontains='Kiralık')
    if 'btnSubmit' in request.POST:
        if True:
            nerden= 'Taşhan Emlak iletişim formu mesajı-Central Web Agency'
            name = request.POST.get('name')
            type = request.POST.get('type')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            messages = request.POST.get('messages')

            subject = 'Contact Page Costumer Back'
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email,"djangomarmaris@gmail.com","info@tashanemlakinsaat.com"]
            contact_message = "\nNerden:%s\nName:%s\nEmail:%s\nTipi:%s\nPhone:%s\nMessages:%s" % (
                nerden,
                name,
                email,
                type,
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



def work_list(request):
    sender = Category.objects.all()
    products = Works.objects.all()
    saleminilistnavbar = Product.objects.filter(type__name__icontains='Satılık')
    rentminilistnavbar = Product.objects.filter(type__name__icontains='Kiralık')


    context = {
        'products':products,
        'sender':sender ,
        'saleminilistnavbar':saleminilistnavbar,
        'rentminilistnavbar':rentminilistnavbar
    }

    return render(request,'central/work.html',context)