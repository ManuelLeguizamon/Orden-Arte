from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView, FormView
from django.contrib.auth.models import User  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import SignupForm
# from .models import Usuario


#---------------------------------------------------------------------------------------------------------
class UsuarioView(LoginRequiredMixin, TemplateView):
    template_name='usuario.html'

#---------------------------------------------------------------------------------------------------------

class SignUpView(FormView):
    template_name = "signup.html"
    form_class = SignupForm
    success_url = reverse_lazy("usuario")

    def form_valid(self, form):
         user = form.save()
         login(self.request, user)
         messages.success(self.request, "Cuenta creada con exito")
         return super().form_valid(form)

#---------------------------------------------------------------------------------------------------------        
class LoginView(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            email = request.POST.get('email')
            password = request.POST.get('contraseña1')

            usuario = authenticate(request, username=email, password=password)
            if usuario is None:
                return render(request, self.template_name, {'errorLogin': 'No se pudo iniciar sesión'})
            else:
                login(request, usuario)
                return redirect('usuario')


"""
#LOGIN PARA VALIDAR CON EL AD DE LA MAQUINA VIRTUAL 
class LoginView(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('contraseña1')

        usuario = authenticate(request, username=username, password=password)

        if usuario is None:
            return render(request, self.template_name, {
                'errorLogin': 'Credenciales incorrectas o usuario no autorizado'
            })
        else:
            login(request, usuario)
            return redirect('usuario')
"""
#---------------------------------------------------------------------------------------------------------
def logout_view(request):
        logout(request)
        return redirect('login')