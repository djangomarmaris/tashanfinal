from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from places.fields import PlacesField

# Create your models here.
MODEL = (
        ('Konut', 'Konut'),
        ('İş Yeri', 'İş Yeri'),
        ('Arsa', 'Arsa'),
        ('Turizm', 'Turizm'),
        ('Bina', 'Bina'),
        )

STATUS  = (
        ('Satılık', 'Satılık'),
        ('Kiralık', 'Kiralık'),)



ROOM  = (
        ('1+0', '1+0'),
        ('1+1', '1+1'),
        ('2+1', '2+1'),
        ('3+1', '3+1'),
        ('4+1', '4+1'),
        ('5+1', '5+1'),
        ('6+1', '6+1'),
        ('7+1', '7+1'),
        ('3+2', '3+2'),
        ('4+2', '4+2'),
        ('5+2', '5+2'),)


class Type(models.Model):
    name = models.CharField(max_length=10,choices=STATUS,default='Taşınmazın Durumunu Giriniz')
    slug = models.SlugField(max_length=200, db_index=True)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=10,default='Şehir Giriniz')

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=10,default='İlçeyi Giriniz')

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=10, choices=ROOM)

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=10,choices=MODEL)
    model = models.CharField(max_length=200, db_index=True,default='Modeli Yazınıcız')
    slug = models.SlugField(max_length=200, db_index=True)


    def __str__(self):
        return self.name

class  Agent(models.Model):
    name = models.CharField(max_length=150,default='İsim/Soyisim')
    phone = models.CharField(max_length=150,default='Telefon')
    email = models.CharField(max_length=150,default='Email')
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)


    def __str__(self):
        return self.name


class Product(models.Model):
    available = models.BooleanField(default=True)
    type =models.ForeignKey(Type, on_delete=models.CASCADE)
    city =models.ForeignKey(City, on_delete=models.CASCADE)
    region =models.ForeignKey(Region, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=150,default='Ürünün İsmi')
    header = models.CharField(max_length=150,default='Ürünün İsmi')
    info = RichTextUploadingField(blank=True)
    adress = models.CharField(max_length=150,default='Evin Tam Adresi')
    location = PlacesField()
    bedrooms  = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    garage = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    house3d = models.BooleanField(default=False)
    m2 = models.IntegerField(default=0)
    build = models.CharField(max_length=150,default='Yapılış Yılı')
    floor = models.CharField(max_length=150,default='Kat')
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    opportunity = models.BooleanField(default=False)
    slider = models.BooleanField(default=False)
    sea = models.BooleanField(default=False, verbose_name='Denize Sıfır')
    hospital = models.BooleanField(default=False, verbose_name='Hastane')
    citycenter = models.BooleanField(default=False, verbose_name='Şehir Merkezi')
    municipality = models.BooleanField(default=False, verbose_name='Belediye')
    pharmacy = models.BooleanField(default=False, verbose_name='Eczane')
    market = models.BooleanField(default=False, verbose_name='Market')
    park = models.BooleanField(default=False, verbose_name='Park')
    fitness = models.BooleanField(default=False, verbose_name='Spor Salonu')
    mosque = models.BooleanField(default=False, verbose_name='Cami')
    seo = models.CharField(max_length=500, default="Seo için Bilgi Giriniz.")
    key = models.CharField(max_length=550, default="Keyword için Giriş")
    slug = models.SlugField(max_length=200, db_index=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('realestate:product_detail', args=[self.slug,self.id])



class Comment(models.Model):
    name = models.CharField(max_length=150, default='İsim/Soyisim')
    postion = models.CharField(max_length=150, default='Mesleği')
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    comment = models.CharField(max_length=500, default="Yorum Giriniz.")


    def __str__(self):
        return self.name




class Images(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title




class Works(models.Model):
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')


    def __str__(self):
        return self.title