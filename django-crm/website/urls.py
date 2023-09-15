from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('add/', views.add_employee, name="add_employee"),
    path('get/<int:id>', views.get_employee, name="get_employee"),
    path('update/<int:id>', views.update_employee, name="update_employee"),
    path('delete/<int:id>', views.delete_employee, name="delete_employee"),
]
