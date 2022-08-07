from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views




app_name = 'realestate'


urlpatterns =[
    path('',views.index,name ='index'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('property/list/',views.product_list,name='product_list'),
    path('property/list/sale/<str:category_slug>/',views.product_sale,name='product_list_sale'),
    path('property/list/rent/<str:category_slug>/',views.product_rent,name='product_list_rent'),
    path('property/detail/<str:slug>/<int:id>',views.product_detail,name='product_detail'),
    path('filter/',views.filter,name='filter')
]


