from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from .models import *


class ToppingForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        validators=[RegexValidator(r'^[a-zA-Z ]+$', 'Only letters and spaces are allowed.')],
        help_text='Enter the name of the topping (letters and spaces only)',
    )

    class Meta:
        model = Topping
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        # Check if the name is unique
        if Topping.objects.filter(name__iexact=name).exists():
            raise ValidationError("Topping name already exists.")
        return name
    

class PizzaForm(forms.Form):
    toppings = forms.ModelChoiceField(queryset=Topping.objects.all() )

    class Meta:
        model = Pizza
        fields = '__all__'


# class PizzaForm(forms.Form):
#     PizzaName = forms.CharField(max_length=100)
#     Toppings = forms.ChoiceField(Topping)
