
from tempfile import template
from .models import Task, Category
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


from django.urls import reverse_lazy

# Create your views here.

class Login(LoginView):
     template_name = "base/login.html"
     fields = '__all__'
     redirect_authenticated_user = True

     def get_success_url(self):
          return reverse_lazy('tasks')


class Register(FormView):
     template_name = "base/register.html"
     form_class = UserCreationForm
     redirect_authenticated_user = True
     success_url = reverse_lazy('tasks')

     def form_valid(self, form):
          user = form.save()
          if user is not None:
               login(self.request, user)
          return super(Register, self).form_valid(form)

     def get(self, *args, **kwargs):
          if self.request.user.is_authenticated:
               return redirect('tasks')
          return super(Register, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin,ListView):
     model = Task
     context_object_name = "tasks"
     template_name = "base/tasks.html"

     def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context['tasks'] = context['tasks'].filter(user=self.request.user)
          context['count'] = context['tasks'].filter(complete=False).count()

          search_input = self.request.GET.get('search') or ''
          if search_input:
               context['tasks'] = context['tasks'].filter(
                title__icontains=search_input)

          context['search_input'] = search_input
          return context
          

class CategoryList(LoginRequiredMixin,ListView):
     model = Category
     context_object_name = "categories"
     template_name = "base/categories.html"

     def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context['categories'] = context['categories'].filter(Category_User = self.request.user)

          search_input = self.request.GET.get('search') or ''
          if search_input:
               context['categories'] = context['categories'].filter(
                Header__icontains=search_input)

          context['search_input'] = search_input
          

          return context

class DetailTask(LoginRequiredMixin,DetailView):
     model = Task
     context_object_name = "task"
     template_name = "base/task.html"

     def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context['tasks'] = context['tasks'].filter(user=self.request.user)
          return context

class DetailCategory(LoginRequiredMixin,DetailView):
     model = Category
     context_object_name = "category"
     template_name = "base/category.html"

     def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context['categories'] = context['categories'].filter(Category_User = self.request.user)
          return context

class CreateTask(LoginRequiredMixin,CreateView):
     model = Task
     fields = ['title', 'description', 'complete']
     success_url = reverse_lazy('tasks')

     def form_valid(self, form):
          form.instance.user = self.request.user
          return super(CreateTask, self).form_valid(form)


class CreateCategory(LoginRequiredMixin,CreateView):
     model = Category
     fields = ['Header']
     success_url = reverse_lazy('categories')

     def form_valid(self, form):
          form.instance.Category_User = self.request.user
          return super(CreateCategory, self).form_valid(form)

class TaskUpdateView(LoginRequiredMixin,UpdateView):
     model = Task
     fields = ['title', 'description', 'complete']
     success_url = reverse_lazy('tasks')

class CategoryUpdateView(LoginRequiredMixin,UpdateView):
     model = Category
     fields = ['Header']
     success_url = reverse_lazy('categories')


class TaskDeleteView(LoginRequiredMixin,DeleteView):
     model = Task
     context_object_name = "task"
     success_url = reverse_lazy('tasks')
     template_name = "base/taskdeleteconfirm.html"

class CategoryDeleteView(LoginRequiredMixin,DeleteView):
     model = Category
     context_object_name = "category"
     success_url = reverse_lazy('categories')
     template_name = "base/categorydeleteconfirm.html"
