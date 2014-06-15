__author__ = 'stefan'
from django.contrib import admin
from models import Product,Category
from forms import ProductAdminForm

class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm

    # sets value for how the admin site lists your products
    list_display = ('name', 'price', 'old_price', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-created_at']

    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
#    readonly_fields = ("created_at", "updated_at")
#    exclude = ('created_at', 'updated_at')

    # sets up slug to be generated from product name
    prepopulated_fields = {'slug' : ('name',)}

# register product model with the admin site
admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    # set up values for how admin site lists categories
    list_display = ('name', 'created_at', 'updated_at',)
    list_display_links = ('name', )
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
#    readonly_fields = ('created_at','updated_at')
#    exclude = ('created_at', 'updated_at',)

    # set up slug to be generated from category name
    prepopulated_fields = {'slug' : ('name', )}

admin.site.register(Category, CategoryAdmin)