from django import forms

from .models import Supplier


class SuppliersModelForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['supplier_name', 'location', 'phone_number']
