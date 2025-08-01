from django.contrib import admin
from .models import Customer, Account, Transaction, Loan

# Inlines for related objects
class TransactionInline(admin.TabularInline):
    model = Transaction
    extra = 0
    readonly_fields = ('transaction_id', 'transaction_date')
    fields = ('transaction_type', 'amount', 'transaction_date', 'served_by', 'description')


class LoanInline(admin.TabularInline):
    model = Loan
    extra = 0
    readonly_fields = ('loan_id', 'date_approved')
    fields = ('loan_type', 'amount', 'loan_balance', 'loan_status', 'date_approved')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'salutation',
        'first_name',
        'middle_name',
        'last_name',
        'email',
        'phone_number',
    )
    search_fields = ('first_name', 'last_name', 'email', 'id_number')
    list_filter = ('salutation', 'country', 'city')
    ordering = ('last_name',)
    

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'account_number',
        'customer',
        'account_type',
        'balance',
        'status',
        'date_opened',
    )
    search_fields = ('account_number', 'customer__first_name', 'customer__last_name')
    list_filter = ('account_type', 'status', 'date_opened')
    inlines = [TransactionInline, LoanInline]


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'transaction_id',
        'transaction_type',
        'amount',
        'transaction_date',
        'account',
        'served_by',
    )
    search_fields = ('transaction_id', 'account__account_number', 'served_by')
    list_filter = ('transaction_type', 'transaction_date')
    readonly_fields = ('transaction_id', 'transaction_date')


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = (
        'loan_id',
        'account',
        'loan_type',
        'amount',
        'loan_balance',
        'loan_status',
        'date_approved',
    )
    search_fields = ('loan_id', 'account__account_number')
    list_filter = ('loan_type', 'loan_status', 'date_approved')
    readonly_fields = ('loan_id', 'date_approved')
