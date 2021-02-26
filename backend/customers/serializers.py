from rest_framework.serializers import ModelSerializer
from customers.models import Customers


class CustomersSerializer(ModelSerializer):
    class Meta:
        model = Customers
        fields = ["id", "name", "age", "city"]
