from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=300)
    price=models.FloatField(default=0)
    description=models.TextField()
    count=models.IntegerField(default=0)
    is_active=models.BooleanField(default=False)

    def to_json(self):
        return {
            'id': self.id,
            'name':self.name,
            'price':self.price,
            'description':self.description,
            'count': self.count,
            'is_active': self.is_active
        }


class Category(models.Model):
    name=models.CharField(max_length=300)

    class Meta:
        verbose_name="Category"
        verbose_name_plural="Categories"

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Company(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    city=models.CharField(max_length=50)
    address=models.TextField()

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def to_json(self):
        return {
            'name':self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }

class Vacancy(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    salary=models.FloatField(default=0)
    company=models.ForeignKey(Company,on_delete=models.CASCADE,null=True)

    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"

    def to_json(self):
        return {
            'name':self.name,
            'description': self.description,
            'salary': self.salary,
            'company': self.company.name
        }
