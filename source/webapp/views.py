from django.shortcuts import render, redirect
# from webapp.models import Post
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
# # from webapp.forms import FoodForm, OrderUpdateForm, OrderCreateForm, OrderFoodForm, StatusUpdateForm
# from django.urls import reverse, reverse_lazy
# from django.shortcuts import redirect, get_object_or_404
# from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# from django.http import JsonResponse


# Create your views here.

def welcome_view(request):
    return render(request, 'welcome.html')

def post_view(request):
    return render(request, 'post_list.html')

# class PostListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
#     model = Post
#     template_name = 'food_list.html'
#     # permission_required = 'webapp.view_food'
