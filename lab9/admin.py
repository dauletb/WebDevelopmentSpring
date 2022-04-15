from django.contrib import admin
from .models import Product, Category, Company, Vacancy


# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Vacancy)
