from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages


def Toppings(request):
    if request.method == 'POST':
        form = ToppingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            Topping.objects.create(name=name)
            messages.success(request, f'Toppings {name} added successful')
            return redirect('Toppings')
    else:
        form = ToppingForm()
    toppings = Topping.objects.all()
    context = {'toppings': toppings, 'form': form}
    return render(request, 'toppings/Toppings.html', context)

def updateToppings(request, pk):
    topping = Topping.objects.get(id=pk)
    form = ToppingForm(instance=topping)
    if request.method == 'POST':
        form = ToppingForm(request.POST or None, instance=topping)
        if form.is_valid():
            # Check if there is already a topping with the same name
            if Topping.objects.filter(name=form.cleaned_data['name']).exclude(id=pk).exists():
                form.add_error('name', 'A topping with this name already exists.')
            else:
                form.save()
                messages.success(request, f'Toppings is updated to {topping} ')
                return redirect('Toppings')
        else:
            messages.success(request, f'No Changes on {topping}')
            return redirect('Toppings')

    return render(request, 'toppings/updateToppings.html', {'form': form})


def deletetopping(request, pk):
    topping = get_object_or_404(Topping, id=pk)
    if request.method == 'POST':
        topping.delete()
        messages.success(request, f'Toppings {topping} deleted Successful')
        return redirect('Toppings')
    
    return render(request, 'toppings/deleteToppings.html', {'topping': topping})