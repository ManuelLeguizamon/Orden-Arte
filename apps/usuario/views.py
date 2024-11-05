from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User  
from django.contrib.auth import authenticate, login, logout

#---------------------------------------------------------------------------------------------------------
class UsuarioView(TemplateView):
    template_name='usuario.html'    

#---------------------------------------------------------------------------------------------------------
class SignUpView(TemplateView): 
    template_name = 'signup.html'

    def post(self, request, *args, **kwargs):
        if request.POST['contraseña1'] == request.POST['contraseña2']:
            try:
                usuario = User.objects.create_user(username=request.POST.get('email'), password=request.POST.get('contraseña1'))
                usuario.save()
                return render(request, 'signup.html', {'exito': 'Usuario creado correctamente'})
            except:
                return render(request, 'signup.html',
                    {'error':'El usuario ya existe'})
        else:
            return render(request, 'signup.html', {
                'error': 'Las contraseñas deben ser iguales'
            })

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

#---------------------------------------------------------------------------------------------------------            
def logout_view(request):
        logout(request)
        return redirect('login')