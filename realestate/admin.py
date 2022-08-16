from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import  Type,City,Region,Category,Product,Agent,Comment , Room ,Images ,Works
# Register your models here.



class Gallery(admin.TabularInline):
    model = Images





class RoomAdmin(admin.ModelAdmin):
    list_display = ['name']

class TypeAdmin(admin.ModelAdmin):
    list_display = ['name']

class CityAdmin(admin.ModelAdmin):
    list_display = ['name']


class RegionAdmin(admin.ModelAdmin):
    list_display = ['name']



class ProdcutAdmin(admin.ModelAdmin):
    list_display = ['name','m2','room','price','available']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['available','price']
    inlines = (Gallery,)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('model',)}



class AgentAdmin(admin.ModelAdmin):
    list_display = ['name']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name']


class WorksAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(Room,RoomAdmin)
admin.site.register(Agent,AgentAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProdcutAdmin)
admin.site.register(Type,TypeAdmin)
admin.site.register(City,CityAdmin)
admin.site.register(Region,RegionAdmin)
admin.site.register(Works,WorksAdmin)

admin.site.site_title = 'Central Web Agency'
admin.site.site_header = 'Taşhan Emlak'
