from django.contrib import admin

# Register your models here.
from core.erp.models import Category, Customer, Product, Sale, SaleDetail

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(SaleDetail)
