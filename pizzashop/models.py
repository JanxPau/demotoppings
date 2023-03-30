from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Topping(models.Model):
    name = models.CharField(max_length=255, unique=True, validators=[RegexValidator(r'^[a-zA-Z ]+$', 'Only letters and spaces are allowed.')])  # define a field for the name of the topping

    def __str__(self):
        return self.name  # return the name of the topping as a string

class Pizza(models.Model):
    name = models.CharField(max_length=100, unique=True, validators=[RegexValidator(r'^[a-zA-Z ]+$', 'Only letters and spaces are allowed.')])  # define a field for the name of the pizza
    Toppings = models.ManyToManyField(Topping)  # define a many-to-many relationship with toppings

    def __str__(self):
        # create a list of topping names separated by commas using a list comprehension
        toppings_list = ', '.join(topping.name for topping in self.Toppings.all())
        return (f'{self.name} with {toppings_list}')  # return the name of the pizza with the list of toppings as a string

    # def __init___(self):
    #     self.pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    #     self.topping = models.ForeignKey(Topping, on_delete=models.SET_NULL, blank=True, null=True)

    #     def __str__(self):
    #         return f'{self.pizza.name} with {self.topping.name}'