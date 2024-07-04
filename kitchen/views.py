from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

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
