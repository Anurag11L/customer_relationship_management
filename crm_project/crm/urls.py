# crm/urls.py
from django.urls import path
from .views import customer_list, create_customer, edit_customer, delete_customer

app_name = 'crm'

urlpatterns = [
    path('', customer_list, name='customer_list'),
    path('customer-list/', customer_list, name='customer_list'),
    path('create-customer/', create_customer, name='create_customer'),
    path('edit-customer/<int:customer_id>/', edit_customer, name='edit_customer'),
    path('delete-customer/<int:customer_id>/', delete_customer, name='delete_customer'),
    # ... (other URL patterns)
]

