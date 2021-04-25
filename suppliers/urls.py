from django.urls import path

from .views import supplier_view, supplier_delete_view

urlpatterns = [
    path('', supplier_view, name='supplier'),
    path('<int:supplier_id>/', supplier_view, name="supplier_edit"),
    path('delete/<int:supplier_id>/', supplier_delete_view, name="supplier_delete"),
]
