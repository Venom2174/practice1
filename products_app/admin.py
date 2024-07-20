from django.contrib import admin
from .models import ProductCategory, Product, Basket

admin.site.register(ProductCategory)
# admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=("name","quanity","price","category")
    search_fields=("name",)
    fields=("name","image","description","price","quanity","category")

class BasketAdmin(admin.TabularInline):
    model=Basket
    extra=0