from django.urls import path
from customers.views import CustomersListView, CustomersRetrieveUpdateView

urlpatterns = [
    path("<int:pk>", CustomersRetrieveUpdateView.as_view()),
    path("", CustomersListView.as_view()),
]
