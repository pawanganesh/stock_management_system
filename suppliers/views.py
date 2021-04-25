from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .forms import SuppliersModelForm
from .models import Supplier


def supplier_view(request, supplier_id=None):
    context = {}
    if request.POST:
        if supplier_id is not None:
            supplier_object = get_object_or_404(Supplier, id=supplier_id)
            form = SuppliersModelForm(request.POST, instance=supplier_object)
        else:
            form = SuppliersModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("supplier")
    else:
        if supplier_id is None:
            form = SuppliersModelForm()
        else:
            supplier_object = get_object_or_404(Supplier, id=supplier_id)
            form = SuppliersModelForm()
            context['supplier_object'] = supplier_object
            # context = {'user_object': user_object}
    suppliers = Supplier.objects.all()
    context['title'] = 'Branch'
    context['supplier_form'] = form
    context['suppliers'] = suppliers

    return render(request, 'suppliers/supplier.html', context)


def supplier_delete_view(request, supplier_id):
    if request.POST:
        supplier_object = get_object_or_404(Supplier, id=supplier_id)
        supplier_object.delete()
        return redirect("supplier")
    return HttpResponse("Cannot perform delete operation")
