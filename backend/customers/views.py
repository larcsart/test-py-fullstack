from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from customers.models import Customers
from customers.serializers import CustomersSerializer


class CustomersListView(ListAPIView):
    queryset = Customers.objects.all().order_by("id")
    serializer_class = CustomersSerializer


class CustomersRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
