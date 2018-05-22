from django import forms
from .models import TestLoans, Loans


class TestLoansForm(forms.ModelForm):
    test = forms.ModelChoiceField(queryset=Loans.objects.values('current_balance', 'original_balance'), initial=0)

    def __init__(self, *args, **kwargs):
        super(TestLoansForm, self).__init__(*args, **kwargs)

    class Meta:
        model = TestLoans
        fields = '__all__'
