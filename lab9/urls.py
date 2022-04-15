from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', views.say_welcome),
    path('products/', views.products_list),
    path('products/<int:pr_id>', views.product_detail),
    path('category/', views.products_category),
    path('category/<int:categ_id>', views.product_concrete_category),
    path('companies/', views.companies),
    path('companies/<int:comp_id>', views.company_id),
    path('companies/<int:com_id>/vacancies', views.vacancies_in_comp),
    path('vacancies/', views.vacs),
    path('vacancies/<int:vac_id>', views.vacs_id),
    path('vacancies/top_ten', views.vacs_topTen)
]