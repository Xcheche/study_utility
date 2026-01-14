from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, FormView

# Create your views here.


# ==================================#
##########Home======================#
# =================================#
class HomeView(TemplateView):
    template_name = "dashboard/home.html"


# ==================================#
##########Register=====================#
# =================================#
class RegisterView(TemplateView):
    template_name = "dashboard/register.html"


# ===================================#
# ================Login View =============#
# ===================================#
class LoginView(TemplateView):
    template_name = "dashboard/login.html"


