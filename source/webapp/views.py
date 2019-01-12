from django.shortcuts import render, redirect
from webapp.models import Post, UserInfo
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from webapp.forms import PostForm, UserForm
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.http import HttpResponseRedirect


# Create your views here.

def welcome_view(request):
    return render(request, 'welcome.html')

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'post_list.html'

    def get_queryset(self):
        return self.model.objects.order_by('-date')


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:post_detail', kwargs={'pk': self.object.pk})



class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_update.html'
    form_class = PostForm

    def dispatch(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if post.author != self.request.user:
            return HttpResponseRedirect(reverse('webapp:post_detail', kwargs={'pk': pk}))
        return super().dispatch(request, pk=pk)

    def get_success_url(self):
        return reverse('webapp:post_detail', kwargs={'pk': self.object.pk})


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'

    def dispatch(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if post.author != self.request.user:
            return HttpResponseRedirect(reverse('webapp:post_detail', kwargs={'pk': pk}))
        return super().dispatch(request, pk=pk)

    def get_success_url(self):
        return reverse('webapp:post_list')



class UserListView(ListView):
    model = UserInfo
    template_name = 'user_list.html'



class UserDetailView(DetailView):
    model = UserInfo
    template_name = "user_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.object.user.posts_by_user.all().order_by('-date')
        return context



class UserUpdateView(UpdateView):
    model = UserInfo
    template_name = 'user_update.html'
    form_class = UserForm

    def get(self, request, pk):
        userinfo = get_object_or_404(UserInfo, pk=pk)
        if userinfo.user != self.request.user:
            return HttpResponseRedirect(reverse('webapp:user_detail', kwargs={'pk': pk}))
        return super().get(request, pk=pk)

    def get_success_url(self):
        return reverse('webapp:user_detail', kwargs={'pk': self.object.pk})


