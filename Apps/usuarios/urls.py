from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from Apps.usuarios.views import ListadoUsuario, registrarUsuario, EditarUsuario, EliminarUsuario
urlpatterns = [
    path('listado_usuarios/', ListadoUsuario.as_view(), name='listado_usuarios'),
    path('registrar_usuarios/', registrarUsuario.as_view(), name='registrar_usuarios'),
    path('actualizar_usuarios/<int:pk>/', EditarUsuario.as_view(), name='actualizar_usuarios'),
    path('eliminar_usuarios/<int:pk>/', EliminarUsuario.as_view(), name='eliminar_usuarios'),
    
]

#urls de vistas implicitas

urlpatterns +=[
    path('Inicio_usuario/', login_required(TemplateView.as_view(
            template_name= 'usuarios/listar_usuarios.html'
        )), name='Inicio_usuario'),
    
]