from django.urls import path

from .views import *


urlpatterns = [
    path('', ListCategoriesView.as_view()),
    path('new-category', CreateNewCategory.as_view()),
]
