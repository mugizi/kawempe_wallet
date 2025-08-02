from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
)     
from .models import Customer, Account, Transaction, Loan
from .forms import (
    CustomerForm, AccountForm, TransactionForm, LoanForm
)

class HomeView(TemplateView):
    template_name = 'index.html'

# Customer Views
class CustomerListView(ListView):
    model = Customer
    template_name = 'bank/customer_list.html'
    context_object_name = 'customers'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'bank/customer_detail.html'
    context_object_name = 'customer'

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'bank/customer_form.html'
    success_url = reverse_lazy('customer_list')

class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'bank/customer_form.html'
    success_url = reverse_lazy('customer_list')

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'bank/customer_confirm_delete.html'
    success_url = reverse_lazy('customer_list')

# Account Views
class AccountListView(ListView):
    model = Account
    template_name = 'bank/account_list.html'
    context_object_name = 'accounts'

class AccountDetailView(DetailView):
    model = Account
    template_name = 'bank/account_detail.html'
    context_object_name = 'account'

class AccountCreateView(CreateView):
    model = Account
    form_class = AccountForm
    template_name = 'bank/account_form.html'
    success_url = reverse_lazy('account_list')

class AccountUpdateView(UpdateView):
    model = Account
    form_class = AccountForm
    template_name = 'bank/account_form.html'
    success_url = reverse_lazy('account_list')

class AccountDeleteView(DeleteView):
    model = Account
    template_name = 'bank/account_confirm_delete.html'
    success_url = reverse_lazy('account_list')

# Transaction Views
class TransactionListView(ListView):
    model = Transaction
    template_name = 'bank/transaction_list.html'
    context_object_name = 'transactions'

class TransactionCreateView(CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'bank/transaction_form.html'
    success_url = reverse_lazy('transaction_list')

# Loan Views
class LoanListView(ListView):
    model = Loan
    template_name = 'bank/loan_list.html'
    context_object_name = 'loans'

class LoanCreateView(CreateView):
    model = Loan
    form_class = LoanForm
    template_name = 'bank/loan_form.html'
    success_url = reverse_lazy('loan_list')