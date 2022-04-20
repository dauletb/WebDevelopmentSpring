from django.contrib import admin
from django.urls import path
from . import views, viewsProj
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('admin/', admin.site.urls),
    path('welcome/', views.say_welcome),
    path('products/', views.products_list),
    path('products/<int:pr_id>', views.product_detail),
    path('category/', views.products_category),
    path('category/<int:categ_id>', views.product_concrete_category),
    path('companies/', views.CompanyAPIView.as_view()),
    path('companies/<int:comp_id>', views.CompanyIDAPIView.as_view()),
    path('companies/<int:com_id>/vacancies', views.VacsInCompsVIEW.as_view()),
    path('vacancies/', views.VacanciesAPIView.as_view()),
    path('vacancies/<int:vac_id>', views.VacanciesIDAPIView.as_view()),
    path('vacancies/top_ten', views.vacs_topTen),
    path('pizzas/', viewsProj.pizza),
    path('desserts/', viewsProj.dessert),
    path('sets/', viewsProj.SetsAPIView.as_view()),
    path('dishes/',viewsProj.DishesAPIView.as_view())
]