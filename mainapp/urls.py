from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.main_page, name="mainpage"),
    path('signup/', views.signup, name="signup"),
    path('login/',auth_views.LoginView.as_view(template_name='main/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='mainpage'), name="logout"),
    path('todolist/', views.todolist, name="todolist"),
    path('completed/', views.completed, name="completed"),
    path('todolist_process/', views.todolist_process, name='todolist_process'),
    path('do_completed/<int:id>', views.do_completed, name="do_completed"),
    path('change_status/<int:id>', views.change_status, name='change_status'),
    path('delete/<int:id>', views.delete, name='delete'),
]
