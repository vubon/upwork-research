from django.contrib import admin

from .models import Loans, TestLoans
from .forms import TestLoansForm
# Register your models here.


class TestLoanAdmin(admin.ModelAdmin):
    form = TestLoansForm


admin.site.register(Loans)
admin.site.register(TestLoans, TestLoanAdmin)
