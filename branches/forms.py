from django import forms

from .models import Branch


class BranchModelForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['branch_name', 'location', 'phone_number']
