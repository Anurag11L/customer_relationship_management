# crm/views.py
from django.shortcuts import render,redirect
from .models import Customer
from django.http import HttpResponse

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'crm/customer_list.html', {'customers': customers})

def create_customer(request):
    if request.method == 'POST':
        # Handle form submission (create a new customer)
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        # Create a new customer in the database
        Customer.objects.create(name=name, email=email, phone=phone, address=address)

        # Redirect to the customer list page after creating a new customer
        return redirect('crm:customer_list')

    # If the request method is not POST, render the form
    return render(request, 'crm/create_customer.html')


from .forms import CustomerForm

def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('crm:customer_list')
    else:
        form = CustomerForm(instance=customer)

    return render(request, 'crm/edit_customer.html', {'form': form, 'customer': customer})

from django.shortcuts import get_object_or_404
from django.http import JsonResponse

def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    customer.delete()
    return JsonResponse({'message': 'Customer deleted successfully'})