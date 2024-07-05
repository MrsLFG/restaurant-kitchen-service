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
