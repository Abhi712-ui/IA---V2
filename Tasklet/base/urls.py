from django.urls import path
from .views import TaskList, DetailTask, CreateTask, TaskUpdateView, TaskDeleteView, Register
from .views import CategoryList, DetailCategory, CreateCategory, CategoryUpdateView, CategoryDeleteView
from .views import Login
from django.contrib.auth.views import LogoutView

urlpatterns = [
     path('login/', Login.as_view(), name="login"),
     path("register/", Register.as_view(), name="register"),
     path('logout/', LogoutView.as_view(next_page="login"), name="logout"),
     path('', TaskList.as_view(), name="tasks"),
     path('categories', CategoryList.as_view(), name="categories"),
     path('task/<int:pk>/', DetailTask.as_view(), name="task"),
     path('category/<int:pk>/', DetailCategory.as_view(), name="category"),
     path('create-task', CreateTask.as_view(), name="create-task"),
     path('create-category', CreateCategory.as_view(), name="create-category"),
     path("update-task/<int:pk>/", TaskUpdateView.as_view(), name="update-task"),
     path("update-category/<int:pk>/", CategoryUpdateView.as_view(), name="update-category"),
     path("delete-task/<int:pk>/", TaskDeleteView.as_view(), name="delete-task"),
     path("delete-category/<int:pk>/", CategoryDeleteView.as_view(), name="delete-category")
]