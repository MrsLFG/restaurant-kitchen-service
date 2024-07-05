from django.test import TestCase

from kitchen.forms import CookCreationForm, SignUpForm


class FormTests(TestCase):
    def test_cooks_creation_form(self):
        form_data = {
            "username": "new_user",
            "password1": "user12test",
            "password2": "user12test",
            "first_name": "Test first",
            "last_name": "test Last",
            "years_of_experience": 1,
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)


class SignUpFormTest(TestCase):
    def test_form_has_fields(self):
        form = SignUpForm()
        expected_fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "years_of_experience",
        ]
        actual_fields = list(form.fields)
        self.assertSequenceEqual(expected_fields, actual_fields)

    def test_form_validation_for_valid_data(self):
        valid_data = {
            "username": "testuser",
            "first_name": "Test",
            "last_name": "User",
            "email": "test@example.com",
            "password1": "testpassword123",
            "password2": "testpassword123",
            "years_of_experience": 5,
        }
        form = SignUpForm(data=valid_data)
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertEqual(user.username, valid_data["username"])
        self.assertEqual(user.first_name, valid_data["first_name"])
        self.assertEqual(user.last_name, valid_data["last_name"])
        self.assertEqual(user.email, valid_data["email"])
        self.assertEqual(user.years_of_experience, valid_data["years_of_experience"])
