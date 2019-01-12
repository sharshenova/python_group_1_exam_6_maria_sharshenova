from django.shortcuts import render, redirect
from webapp.models import Post
from django.views.generic import ListView, DetailView
#CreateView, UpdateView, DeleteView, FormView
from webapp.forms import PostForm
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse


# Create your views here.

def welcome_view(request):
    return render(request, 'welcome.html')

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'post_list.html'

    # def get_queryset(self):
        #order_by


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'
