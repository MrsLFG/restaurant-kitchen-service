from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import CookCreationForm, CookUpdateExperience, DishForm
from kitchen.models import Cook, Dish, DishType


def index(request: HttpRequest) -> HttpResponse:
    num_cook = Cook.objects.count()
    num_dish = Dish.objects.count()
    num_dish_types = DishType.objects.count()
    context = {
        "num_cook": num_cook,
        "num_dish": num_dish,
        "num_dish_types": num_dish_types,
    }
    return render(request, "kitchen/index.html", context=context)


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "kitchen/dish_type_list.html"
    context_object_name = "dish_type_list"
    paginate_by = 3


class DishTypeCreateView(generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-type-list")
    template_name = "kitchen/dish_type_form.html"


class DishTypeUpdateView(generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-type-list")
    template_name = "kitchen/dish_type_form.html"


class DishTypeDeleteView(generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-type-list")
    template_name = "kitchen/dish_type_confirm_delete.html"


class CookListView(generic.ListView):
    model = Cook
    paginate_by = 3


class CookDetailView(generic.DetailView):
    model = Cook
    queryset = Cook.objects.all().prefetch_related("dishes__dish_type")


class CookCreateView(generic.CreateView):
    model = Cook
    form_class = CookCreationForm


class CookUpdateView(generic.UpdateView):
    model = Cook
    form_class = CookUpdateExperience


class CookDeleteView(generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 3


class DishDetailView(generic.DetailView):
    model = Dish
    queryset = Dish.objects.all().select_related("dish_type")


class DishCreateView(generic.CreateView):
    model = Dish
    form_class = DishForm


class DishUpdateView(generic.UpdateView):
    model = Dish
    form_class = DishForm


class DishDeleteView(generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")

