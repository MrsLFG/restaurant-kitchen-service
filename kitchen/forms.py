from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from kitchen.models import Cook, Dish


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = (UserCreationForm.Meta.fields +
                  ("first_name", "last_name", "years_of_experience",))


class CookUpdateExperience(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ("years_of_experience", )


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Dish
        fields = "__all__"


class DishTypeNameSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name"}
        )
    )


class CookUsernameSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Search by username"}
        )
    )


class DishNameSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name"}
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username*",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email*",
                "class": "form-control"
            }
        ))
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "class": "form-control"
            }
        ), required=False)
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last Name",
                "class": "form-control"
            }
        ), required=False)
    years_of_experience = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Years of Experience",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password*",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check*",
                "class": "form-control"
            }
        ))

    class Meta:
        model = Cook
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "years_of_experience",
        )


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
