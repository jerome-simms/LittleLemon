from django.test import Client, TestCase

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    c = Client()

    def setUp(self):
        Menu.objects.create(title='Test item1', price=3.99, inventory=10)
        Menu.objects.create(title='Test item2', price=12.99, inventory=20)
        Menu.objects.create(title='Test item3', price=8.99, inventory=15)
        Menu.objects.create(title='Test item4', price=6.99, inventory=1)

        objs = Menu.objects.all()
        self.serialized_menu_objs = MenuSerializer(objs, many=True)
    
    def test_getall(self):
        response = self.c.get('/restaurant/menu/')
        
        # check for correct response status code
        self.assertEqual(response.status_code, 200)

        # ensure that the length of the data is the same as the number of Menu objects defined in setUp
        self.assertEqual(len(response.data), 4)

        # check that the response data is the same as the serialized menu_objects data
        self.assertEqual(self.serialized_menu_objs.data, response.data)