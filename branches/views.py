from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .forms import BranchModelForm
from .models import Branch


def branch_view(request, branch_id=None):
    context = {}
    if request.POST:
        if branch_id is not None:
            branch_object = get_object_or_404(Branch, id=branch_id)
            form = BranchModelForm(request.POST, instance=branch_object)
        else:
            form = BranchModelForm(request.POST)
        if form.is_valid():
            # branch = Branch(
            #     branch_name=request.POST['branch_name'],
            #     location=request.POST['location'],
            #     phone_number=request.POST['phone_number']
            # )
            # branch.save()
            form.save()
            return redirect("branch")
    else:
        if branch_id is None:
            form = BranchModelForm()
        else:
            branch_object = get_object_or_404(Branch, id=branch_id)
            form = BranchModelForm()
            context['branch_object'] = branch_object
            # context = {'user_object': user_object}
    branches = Branch.objects.all()
    context['title'] = 'Branch'
    context['branch_form'] = form
    context['branches'] = branches
    # context = {
    #     'title': 'Branch',
    #     'branch_form': form,
    #     'branches': branches,
    # }

    return render(request, 'branches/branch.html', context)


def branch_delete_view(request, branch_id):
    if request.POST:
        branch_object = get_object_or_404(Branch, id=branch_id)
        branch_object.delete()
        return redirect("branch")
    return HttpResponse("Cannot perform delete operation")
