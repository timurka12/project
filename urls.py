from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('registration', RegisterUser.as_view()),
    path('log_in', LoginUser.as_view(), name='log_in'),
    path('logout', logout_user, name='logout'),
    path('One_recipe', show_one_recipe, name='one_recipe'),
    path('One_recipe/<int:pk>', ShowOneRecipe.as_view(), name='ShowOneRecipe'),
    path('create_recipe', RecipeView.as_view(), name='create_recipe'),
    path('delete_recipe/<int:pk>/', DeleteRecipe.as_view(), name='delete_recipe'),
    path('edit_recipe/<int:pk>/', UpdateRecipe.as_view(), name='edit_recipe'),
    path('all_recipe', AllRecipe.as_view(), name='AllRecipe')

]