import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import Http404
from django.http.response import JsonResponse
from rest_framework.response import Response
from .models import Product, Category, Vacancy,Company
from .serializers import CategorySerializer, VacancyModelSerializer, CompanySerializer,CompanyModelSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

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
    data=CategorySerializer(products)
    products_item= [product.to_json() for product in products]
    return JsonResponse(products_item, safe=False)

def product_concrete_category(request,categ_id):
    try:
        product=Category.objects.get(id=categ_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'message:': 'doesnt exist'})
    return JsonResponse(product.to_json())

@api_view(['GET','POST'])
def companies(request):
    if request.method=='GET':
        comps = Company.objects.all()
        companies = CompanySerializer(comps, many=True)
        return Response(companies.data)
    elif request.method=='POST':
        data=json.loads(request.body)
        serializer=CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.error_messages)

class CompanyAPIView(APIView):
    def get(self,request):
        comps = Company.objects.all()
        companies = CompanySerializer(comps, many=True)
        return Response(companies.data)
    def post(self,request):
        data = json.loads(request.body)
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.error_messages)
    

class CompaniesGenView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyModelSerializer


def company_id(request,comp_id):
    try:
        comp=Company.objects.get(id=comp_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'message': 'doesnt exist'})

    if request.method == 'GET':
        comps = CompanySerializer(comp)
        return JsonResponse(comps.data)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = CompanySerializer(instance=comp,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        comp.delete()
        return JsonResponse({'message': 'done'}, status=204)

class CompanyIDAPIView(APIView):
    def get_object(self,comp_id):
        try:
            return Company.objects.get(id=comp_id)
        except Company.DoesNotExist as de:
            raise Http404

    def get(self,request,comp_id=None):
        comp=self.get_object(comp_id)
        serializer=CompanyModelSerializer(comp)
        return Response(serializer.data)

    def put(self,request,comp_id=None):
        comp=self.get_object(comp_id)
        serializer = CompanySerializer(instance=comp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

    def delete(self,request,comp_id=None):
        comp=self.get_object(comp_id)
        comp.delete()


def vacancies_in_comp(request,com_id):
    try:
        comp = Company.objects.get(id=com_id)
        vacancies=[vacs.to_json() for vacs in comp.vacancy_set.all()]
    except Company.DoesNotExist as e:
        return JsonResponse({'message': 'doesnt exist'})
    return JsonResponse(vacancies,safe=False)

class VacsInCompsVIEW(APIView):
    def get_object(self,com_id):
        try:
            return Company.objects.get(id=com_id).vacancy_set.all()
        except Company.DoesNotExist as de:
            raise Http404

    def get(self,request,com_id=None):
        comp=self.get_object(com_id)
        serializer=VacancyModelSerializer(comp,many=True)
        return Response(serializer.data)

    def put(self,request,com_id=None):
        comp=self.get_object(com_id)
        serializer = VacancyModelSerializer(instance=comp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

    def delete(self,request,com_id=None):
        comp=self.get_object(com_id)
        comp.delete()

def vacs(request):
    if request.method=='GET':
        vacancies = Vacancy.objects.all()
        vacs = VacancyModelSerializer(vacancies, many=True)
        return JsonResponse(vacs.data, safe=False)
    elif request.method=='POST':
        data=json.loads(request.body)
        serializer=VacancyModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.error_messages)

class VacanciesAPIView(APIView):
    def get(self,request):
        vacancies = Vacancy.objects.all()
        vacs = VacancyModelSerializer(vacancies, many=True)
        return Response(vacs.data)
    def post(self, request):
        data = json.loads(request.body)
        serializer = VacancyModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.error_messages)

def vacs_id(request,vac_id):
    try:
        vacancy = Vacancy.objects.get(id=vac_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'message': 'doesnt exist'})
    if request.method == 'GET':
        vacs = VacancyModelSerializer(vacancy)
        return JsonResponse(vacs.data)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = VacancyModelSerializer(instance=vacancy,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif request.method=='DELETE':
        vacancy.delete()
        return JsonResponse({'message': 'done'},status=204)

class VacanciesIDAPIView(APIView):
    def get_object(self,vac_id):
        try:
            vacancy = Vacancy.objects.get(id=vac_id)
            return vacancy
        except Vacancy.DoesNotExist as e:
            return JsonResponse({'message': 'doesnt exist'})

    def get(self,request,vac_id=None):
        vacs = self.get_object(vac_id)
        vacancies=VacancyModelSerializer(vacs)
        return Response(vacancies.data)

    def put(self,request,vac_id=None):
        vacs = self.get_object(vac_id)
        serializer = VacancyModelSerializer(instance=vacs,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

    def delete(self,request,vac_id=None):
        vacs = self.get_object(vac_id)
        vacs.delete()



def vacs_topTen(request):
    def compare(d):
        return d['salary']
    vacancies=Vacancy.objects.all()
    topVacs=[vacs.to_json() for vacs in vacancies]
    topVacs.sort(key=compare)
    return JsonResponse(topVacs,safe=False)






