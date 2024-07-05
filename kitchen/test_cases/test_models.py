from django.test import TestCase

from kitchen.models import DishType, Cook, Dish


class TestModels(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(
            name="test"
        )
        self.cook = Cook.objects.create(
            username="test1",
            password="testpass",
            years_of_experience="1"
        )
        self.dish = Dish.objects.create(
            name="Test",
            price=10.00,
            dish_type=self.dish_type
        )
        self.dish.cooks.add(self.cook)

    def test_dish_type_str(self):
        self.assertEqual(
            str(self.dish_type),
            self.dish_type.name
        )

    def test_cook_str(self):
        self.assertEqual(
            str(self.cook),
            f"{self.cook.username} ({self.cook.first_name} {self.cook.last_name})"
        )

    def test_dish_str(self):
        self.assertEqual(
            str(self.dish),
            f"{self.dish.name}: {self.dish.dish_type} ({self.dish.price})"
        )

    def test_create_cook_with_years_of_experience(self):
        cook_with_years_of_experience = Cook.objects.create_user(
            username="test",
            password="pass1",
            years_of_experience=1
        )
        self.assertEqual(
            cook_with_years_of_experience.years_of_experience, 1
        )
        self.assertEqual(cook_with_years_of_experience.username, "test")
