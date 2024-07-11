from django.urls import path
from django.views.generic import TemplateView

from kitchen.views import (
    index,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    CookListView,
    CookDetailView,
    CookCreateView,
    CookUpdateView,
    CookDeleteView,
    DishListView,
    DishDetailView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    AssignUserToDishView,
    CustomLoginView,
)


app_name = "kitchen"

urlpatterns = [
    path("", index, name="index"),
    path(
        "dish-types/",
        DishTypeListView.as_view(),
        name="dish-type-list"
    ),
    path(
        "dish-types/create/",
        DishTypeCreateView.as_view(),
        name="dish-type-create"
    ),
    path(
        "dish-types/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish-type-update"
    ),
    path(
        "dish-types/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete"
    ),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path("cooks/<int:pk>/update/", CookUpdateView.as_view(), name="cook-update"),
    path("cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cook-delete"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path(
        "dishes/<int:pk>/toggle-assign/",
        AssignUserToDishView.as_view(),
        name="dish-assign"),
    path("login/", CustomLoginView.as_view(), name='login'),
    path(
        "sign-in/",
        TemplateView.as_view(template_name='kitchen/sign-in.html'),
        name='sign-in'),
]
