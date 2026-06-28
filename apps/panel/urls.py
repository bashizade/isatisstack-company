from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="panel_index"),
    
    path('users/',views.UserListView.as_view(),name="panel_user_list"),
    path('users/create',views.UserCreateView.as_view(),name="panel_user_create"),
    path('users/update/<int:pk>/',views.UserUpdateView.as_view(),name="panel_user_update"),
    path('users/delete/<int:pk>/',views.UserDeleteView.as_view(),name="panel_user_delete"),
]