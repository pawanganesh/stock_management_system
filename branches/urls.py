from django.urls import path

from .views import branch_view, branch_delete_view

urlpatterns = [
    path('', branch_view, name="branch"),
    path('<int:branch_id>/', branch_view, name="branch_edit"),
    path('delete/<int:branch_id>/', branch_delete_view, name="branch_delete"),
]
