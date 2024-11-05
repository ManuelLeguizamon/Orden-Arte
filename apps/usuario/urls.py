from django.urls import path
from apps.usuario.views import UsuarioView, LoginView, SignUpView, logout_view
urlpatterns = [
    path('', UsuarioView.as_view(), name="usuario"),
    path('login/', LoginView.as_view(), name="login"),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', logout_view, name='logout'),
    ]