from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from apps.main.models import User

from . import forms

# Create your views here.
def index(request):
    return render(request, "panel/index.html")



class UserListView(ListView):
    model = User
    template_name = "panel/users/list.html"
    context_object_name = "users"
    

class UserCreateView(CreateView):
    model = User
    template_name = "panel/users/form.html"
    form_class = forms.UserForm
    success_url = reverse_lazy('panel_user_list')


class UserUpdateView(UpdateView):
    model = User
    template_name = "panel/users/form.html"
    form_class = forms.UserForm
    success_url = reverse_lazy('panel_user_list')
    

class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('panel_user_list')

