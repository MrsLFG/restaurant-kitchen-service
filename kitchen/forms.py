from django import forms
from django.contrib.auth.forms import UserCreationForm

from kitchen.models import Cook


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = (UserCreationForm.Meta.fields +
                  ("first_name", "last_name", "years_of_experience",))


class CookUpdateExperience(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ("years_of_experience", )
