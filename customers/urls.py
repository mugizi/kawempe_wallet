from django import views
from django.urls import path
from .views import (
    HomeView, CustomerListView, CustomerDetailView, CustomerCreateView,
    CustomerUpdateView, CustomerDeleteView,
    AccountListView, AccountDetailView, AccountCreateView,
    AccountUpdateView,
    TransactionListView, TransactionCreateView,
    LoanListView, LoanCreateView, delete_account
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # Customer URLs
    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('customers/add/', CustomerCreateView.as_view(), name='customer_add'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('customers/<int:pk>/edit/', CustomerUpdateView.as_view(), name='customer_edit'),
    path('customers/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),

    # Account URLs
    path('accounts/', AccountListView.as_view(), name='account_list'),
    path('accounts/add/', AccountCreateView.as_view(), name='account_add'),
    path('accounts/<str:pk>/', AccountDetailView.as_view(), name='account_detail'),
    path('accounts/<str:pk>/edit/', AccountUpdateView.as_view(), name='account_edit'),
    path('accounts/<str:pk>/delete/', delete_account, name='account_delete'),


    # Transaction URLs
    path('transactions/', TransactionListView.as_view(), name='transaction_list'),
    path('transactions/add/', TransactionCreateView.as_view(), name='transaction_add'),

    # Loan URLs
    path('loans/', LoanListView.as_view(), name='loan_list'),
    path('loans/add/', LoanCreateView.as_view(), name='loan_add'),
]