from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from random import choice, sample
from django.views import View
from .forms import *
from .models import *


class Index(ListView):
    template_name = 'working_with_recipes/index.html'
    model = Recipe
    recipes_id = set(Recipe.objects.values_list('id', flat=True))
    random_recipes_id = sample(recipes_id, 6)
    context_object_name = 'recipes'
    extra_context = {
        'random_recipes_id': random_recipes_id,
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'working_with_recipes/registration.html'
    success_url = '/log_in'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('one_recipe')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'working_with_recipes/log_in.html'

    def get_success_url(self):
        return reverse_lazy('one_recipe')


def logout_user(request):
    logout(request)
    return redirect('log_in')


def show_one_recipe(request):
    recipes_id = Recipe.objects.values_list('id', flat=True)
    num = choice(recipes_id)
    recipe = get_object_or_404(Recipe, id=num)
    return render(request, 'working_with_recipes/One_recipe.html', {
        'recipe': recipe,
    })


class ShowOneRecipe(DetailView):
    template_name = 'working_with_recipes/One_recipe.html'
    model = Recipe
    context_object_name = 'recipe'


class RecipeView(CreateView):
    model = Recipe
    recipe = Recipe.objects.annotate()
    template_name = 'working_with_recipes/CreateRecipe.html'
    fields = '__all__'
    success_url = '/One_recipe'
    extra_context = {
        'recipe': recipe,
    }


class UpdateRecipe(UpdateView):
    model = Recipe
    fields = '__all__'
    recipe = Recipe.objects.annotate()
    template_name = 'working_with_recipes/CreateRecipeEdit.html'
    success_url = f'/One_recipe'
    extra_context = {
        'recipe': recipe,
    }


class DeleteRecipe(DeleteView):
    model = Recipe
    context_object_name = 'recipe'
    success_url = '/create_recipe'

    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(DeleteRecipe, self).form_valid(form)


class AllRecipe(ListView):
    template_name = 'working_with_recipes/All_Recipe.html'
    model = Recipe
    context_object_name = 'recipes'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset