from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import DishType, Dish


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


class PrivateDishTypeTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test1",
            password="pass1"
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_types(self):
        DishType.objects.create(name="test")
        url = reverse("kitchen:dish-type-list")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        dish_type = DishType.objects.all()
        self.assertEqual(
            list(res.context["dish_type_list"]),
            list(dish_type)
        )
        self.assertTemplateUsed(res, "kitchen/dish_type_list.html")


class PrivateCookTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test2",
            password="pass2"
        )
        self.client.force_login(self.user)

    def test_creation_cooks(self):
        form_data = {
            "username": "new_user",
            "password1": "user12test",
            "password2": "user12test",
            "first_name": "Test first",
            "last_name": "test Last",
            "years_of_experience": 1
        }

        self.client.post(reverse("kitchen:cook-create"), data=form_data)
        new_user = get_user_model().objects.get(
            username=form_data["username"]
        )
        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(
            new_user.years_of_experience,
            form_data["years_of_experience"]
        )


class DishListViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpass123"
        )
        self.dish_type = DishType.objects.create(name="TEST")
        self.dish = Dish.objects.create(
            name="test",
            price=10.00,
            dish_type=self.dish_type
        )
        self.dish.cooks.add(self.user)
        self.client.force_login(self.user)

    def test_dish_list_view_search(self):
        response = self.client.get(
            reverse("kitchen:dish-list"), {"name": "test"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.dish.dish_type.name)
        self.assertContains(response, self.dish.name)

    def test_dish_list_view_pagination(self):
        dish_type = DishType.objects.create(name="Test")
        dishes = [
            Dish.objects.create(
                name=f"name{i}",
                price=10.00,
                dish_type=dish_type
            )
            for i in range(3)
        ]
        for dish in dishes:
            dish.cooks.add(self.user)
        response = self.client.get(reverse("kitchen:dish-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["dish_list"]), 3)
        self.assertTrue(response.context["is_paginated"])
