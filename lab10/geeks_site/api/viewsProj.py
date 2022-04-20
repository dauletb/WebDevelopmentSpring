import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import Http404
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Pizza, Dessert, Set, Dish, SpecialDishes, News
from .serializers import PizzaSerializer, DessertSerializer, SetsModelSerializer, DishesModelSerializer,SpecialDishesModelSerializer,NewsModelSerializer

@api_view(['GET','POST'])
def pizza(request):
    if request.method=='GET':
        pizzas = Pizza.objects.all()
        pizza = PizzaSerializer(pizzas, many=True)
        return Response(pizza.data)
    elif request.method=='POST':
        serializer=PizzaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return Response(serializer.error_messages)

@api_view(['GET','POST'])
def dessert(request):
    if request.method=='GET':
        comps = Dessert.objects.all()
        companies = DessertSerializer(comps, many=True)
        return Response(companies.data)
    elif request.method=='POST':
        serializer=DessertSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error_messages)

class SetsAPIView(APIView):
    def get(self,request):
        vacancies = Set.objects.all()
        vacs = SetsModelSerializer(vacancies, many=True)
        return Response(vacs.data)
    def post(self, request):
        data = json.loads(request.body)
        serializer = SetsModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error_messages)

class DishesAPIView(APIView):
    def get(self,request):
        vacancies = Dish.objects.all()
        vacs = DishesModelSerializer(vacancies, many=True)
        return Response(vacs.data)
    def post(self, request):
        data = json.loads(request.body)
        serializer = DishesModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error_messages)

class SpecialDishesAPIView(APIView):
    def get(self,request):
        vacancies = SpecialDishes.objects.all()
        vacs = SpecialDishesModelSerializer(vacancies, many=True)
        return Response(vacs.data)
    def post(self, request):
        data = json.loads(request.body)
        serializer = SpecialDishesModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error_messages)

class NewsAPIView(APIView):
    def get(self,request):
        vacancies = News.objects.all()
        vacs = NewsModelSerializer(vacancies, many=True)
        return Response(vacs.data)
    def post(self, request):
        data = json.loads(request.body)
        serializer = NewsModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error_messages)

class NewsIDAPIView(APIView):
    def get_object(self,news_id):
        try:
            vacancy = News.objects.get(id=news_id)
            return vacancy
        except News.DoesNotExist as e:
            return JsonResponse({'message': 'doesnt exist'})

    def get(self,request,news_id=None):
        vacs = self.get_object(news_id)
        vacancies=NewsModelSerializer(vacs)
        return Response(vacancies.data)

    def put(self,request,news_id=None):
        vacs = self.get_object(news_id)
        serializer = NewsModelSerializer(instance=vacs,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

    def delete(self,request,news_id=None):
        vacs = self.get_object(news_id)
        vacs.delete()



