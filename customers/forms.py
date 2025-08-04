from django import forms
from .models import Customer, Account, Transaction, Loan

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'salutation', 'first_name', 'middle_name', 'last_name',
            'id_number', 'phone_number', 'email', 'date_of_birth','location'
        ]
        widgets = {
            'salutation':    forms.Select(attrs={'class': 'form-select'}),
            'first_name':    forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name':   forms.TextInput(attrs={'class': 'form-control'}),
            'last_name':     forms.TextInput(attrs={'class': 'form-control'}),
            'id_number':     forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number':  forms.TextInput(attrs={'class': 'form-control'}),
            'email':         forms.EmailInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(
                                 attrs={
                                   'type': 'date',
                                   'class': 'form-control'
                                 }
                              ),
    
            'location':       forms.TextInput(attrs={'class': 'form-control'}),

        }

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            'customer', 'account_type', 'balance', 'status'
        ]

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'transaction_type', 'amount', 'description',
            'account', 'served_by'
        ]

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = [
            'account', 'loan_type', 'amount', 'loan_balance', 'loan_status'
        ]
        