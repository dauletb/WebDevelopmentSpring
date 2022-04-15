from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from .models import Product, Category, Vacancy,Company

def say_welcome(request):
    return HttpResponse('Welcome to my Soul Society')

def products_list(request):
    products= Product.objects.all()
    products_item= [product.to_json() for product in products]
    return JsonResponse(products_item, safe=False)

def product_detail(request, pr_id):
    try:
        product=Product.objects.get(id=pr_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'message:': 'doesnt exist'})
    return JsonResponse(product.to_json())

def products_category(request):
    products= Category.objects.all()
    products_item= [product.to_json() for product in products]
    return JsonResponse(products_item, safe=False)

def product_concrete_category(request,categ_id):
    try:
        product=Category.objects.get(id=categ_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'message:': 'doesnt exist'})
    return JsonResponse(product.to_json())

def companies(request):
    companies=Company.objects.all()
    companies_list=[comp.to_json() for comp in companies]
    return JsonResponse(companies_list, safe=False)

def company_id(request,comp_id):
    try:
        comp=Company.objects.get(id=comp_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'message': 'doesnt exist'})
    return JsonResponse(comp.to_json())

def vacancies_in_comp(request,com_id):
    try:
        comp = Company.objects.get(id=com_id)
        vacancies=[vacs.to_json() for vacs in comp.vacancy_set.all()]
    except Company.DoesNotExist as e:
        return JsonResponse({'message': 'doesnt exist'})
    return JsonResponse(vacancies,safe=False)
def vacs(request):
    vacancies=Vacancy.objects.all()
    vacs=[vacans.to_json() for vacans in vacancies]
    return JsonResponse(vacs,safe=False)

def vacs_id(request,vac_id):
    try:
        vacancy = Vacancy.objects.get(id=vac_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'message': 'doesnt exist'})
    return JsonResponse(vacancy.to_json())
def vacs_topTen(request):
    def compare(d):
        return d['salary']
    vacancies=Vacancy.objects.all()
    topVacs=[vacs.to_json() for vacs in vacancies]
    topVacs.sort(key=compare)
    return JsonResponse(topVacs,safe=False)






