from rest_framework import status
from rest_framework.test import APITestCase
from customers.models import Customers


class CustomersTest(APITestCase):
    fixtures = ["customers/fixtures/customers.json"]

    def test_list_customers(self):
        """
        Test GET /customers and pagination
        """
        request = self.client.get("/customers/")
        expected = [
            {"id": 1, "name": "Caroline Westernick", "age": 21, "city": "NYC"},
            {"id": 2, "name": "Adam Mengol", "age": 31, "city": "London"},
            {
                "id": 4,
                "name": "João Maria José",
                "age": 25,
                "city": "Rio de Janeiro",
            },
            {"id": 5, "name": "Sebastian Urel", "age": 27, "city": "Toronto"},
            {"id": 6, "name": "Leon Colda Dongal", "age": 22, "city": "Ibiza"},
            {
                "id": 11,
                "name": "Ted Honda Connel",
                "age": 33,
                "city": "Amsterdam",
            },
            {"id": 13, "name": "Loriel Merita", "age": 24, "city": "Berlim"},
            {"id": 14, "name": "Spliker Sonik", "age": 46, "city": "Tokio"},
            {
                "id": 15,
                "name": "Fernando Ogawa",
                "age": 30,
                "city": "Porto Alegre",
            },
            {"id": 17, "name": "Abdul Hamid", "age": 48, "city": "Daca"},
        ]
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(expected, request.json()["results"])

        request = self.client.get("/customers/?page=2")
        expected = [
            {"id": 18, "name": "Ariston Alex", "age": 25, "city": "Kaohsiung"},
            {"id": 21, "name": "Chris Arthus", "age": 22, "city": "Naipidau"},
            {"id": 22, "name": "Katty Deanna", "age": 19, "city": "Hanói"},
            {"id": 23, "name": "Emily Ethel", "age": 38, "city": "Katmandu"},
            {"id": 25, "name": "Nico Teofil", "age": 38, "city": "Naggu"},
            {"id": 30, "name": "Calvin Joseph", "age": 38, "city": "Kabul"},
            {"id": 32, "name": "Amberlee Thomas", "age": 38, "city": "Bagdá"},
            {"id": 33, "name": "Jacob Tyler", "age": 38, "city": "Paris"},
        ]

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(expected, request.json()["results"])

    def test_update_customer(self):
        """
        Test PUT /customers/{id}
        """
        request = self.client.put(
            "/customers/1",
            {"name": "Caroline Westernick", "age": 22, "city": "Chicago"},
        )
        expected = {
            "id": 1,
            "name": "Caroline Westernick",
            "age": 22,
            "city": "Chicago",
        }
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        result = Customers.objects.get(id=1)
        self.assertEqual(result.name, expected["name"])
        self.assertEqual(result.age, expected["age"])
        self.assertEqual(result.city, expected["city"])
