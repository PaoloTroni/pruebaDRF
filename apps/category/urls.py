from django.urls import path

from .views import *


urlpatterns = [
    path('', ListCategoriesView.as_view()), #eliminado "categories" para mantener las rutas más limpias y coherentes
    path('new-category', CreateNewCategory.as_view()),
]
