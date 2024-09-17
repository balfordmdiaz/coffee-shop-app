from django.urls import path
from .views import ProductFormView, ProductListView

urlpatterns = [
    path("", ProductListView.as_view(), name="list_product"),
    path("add/", ProductFormView.as_view(), name="add_product"),
]