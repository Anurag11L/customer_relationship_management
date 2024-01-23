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

def edit_customer(request, customer_id):
    # ... (define the logic for editing a customer)
    return HttpResponse(f"Editing customer with ID: {customer_id}")