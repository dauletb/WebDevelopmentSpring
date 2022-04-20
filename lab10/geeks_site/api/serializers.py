from rest_framework import serializers
from .models import Category,Vacancy,Company, Pizza, Dessert, Dish,Set, SpecialDishes, News

class CategorySerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()

    def create(self, validated_data):
        category=Category.objects.create(name=validated_data['name'])
        return category

    def update(self, instance, validated_data):
        instance.name=validated_data['name']
        instance.save()
        return instance

class VacancyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vacancy
        fields=['id','name','description','salary','company']

class CompanySerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    description=serializers.CharField()
    city=serializers.CharField()
    address=serializers.CharField()

    def create(self, validated_data):
        comp=Company.objects.create(name=validated_data['name'])
        return comp
    def update(self, instance, validated_data):
        instance.name=validated_data['name']
        instance.save()
        return instance
class CompanyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields=['id','name','description','city','address']

class PizzaSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    description=serializers.CharField()
    price=serializers.FloatField()
    url=serializers.CharField()

    def create(self, validated_data):
        category = Pizza.objects.create(name=validated_data['name'])
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.save()
        return instance


class DessertSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.FloatField()
    url = serializers.CharField()

    def create(self, validated_data):
        category = Dessert.objects.create(name=validated_data['name'])
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.save()
        return instance


class SetsModelSerializer(serializers.ModelSerializer):
    component1=PizzaSerializer(read_only=True)
    component2=DessertSerializer(read_only=True)
    class Meta:
        model=Set
        fields=['id','name','description','component1','component2','price']

class DishesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dish
        fields=['id','name','description','price']

class SpecialDishesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=SpecialDishes
        fields=['id','name','description','price']

class NewsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=News
        fields=['id','description','date']




