from django.test import TestCase
from django.urls import reverse


class PublicViewsTest(TestCase):
    def setUp(self):
        self.dish_type_list_url = reverse("kitchen:dish-type-list")
        self.dish_type_create_url = reverse("kitchen:dish-type-create")
        self.cook_list_url = reverse("kitchen:cook-list")
        self.cook_create_url = reverse("kitchen:cook-create")
        self.dish_list_url = reverse("kitchen:dish-list")
        self.dish_create_url = reverse("kitchen:dish-create")

    def test_login_required(self):
        urls = [
            self.dish_type_list_url,
            self.dish_type_create_url,
            self.cook_list_url,
            self.cook_create_url,
            self.dish_list_url,
            self.dish_create_url
        ]

        for url in urls:
            res = self.client.get(url)
            self.assertNotEqual(res.status_code, 200)



