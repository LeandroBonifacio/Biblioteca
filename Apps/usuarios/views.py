import json
from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.serializers import serialize
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from Apps.usuarios.models import Usuario
from .forms import FormularioLogin, FormularioUsuario
# Create your views here.

class inicio(LoginRequiredMixin,TemplateView):
    template_name = 'index.html'

class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)


def Logout(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')

class ListadoUsuario(LoginRequiredMixin,ListView):
    model = Usuario

    def  get_queryset(self):
        return self.model.objects.filter(usuario_activo = True)
    
    def get(self, request, *args,**kwargs):
        if request.is_ajax():
            data = serialize('json', self.get_queryset())
            return HttpResponse(data, 'application/json')
        else:
             return redirect('usuarios:Inicio_usuario')

class registrarUsuario(LoginRequiredMixin,CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuarios/crear_usuario.html'

    def post(self, request, *args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                nuevo_usuario = Usuario(
                    email = form.cleaned_data.get('email'),
                    username = form.cleaned_data.get('username'),
                    nombres = form.cleaned_data.get('nombres'),
                    apellidos = form.cleaned_data.get('apellidos')
                )
                nuevo_usuario.set_password(form.cleaned_data.get('password1'))
                nuevo_usuario.save()
                mensaje =f'{self.model.__name__} registrado correctamente'
                error = 'No hay error'
                response = JsonResponse({'mensaje':mensaje, 'error':error})
                response.status_code = 201
                return response
            else:
                mensaje =f'{self.model.__name__} no se ha podido registrar'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje, 'error':error})
                response.status_code = 400
                return response
        else:
            return redirect('usuarios:Inicio_usuario')

class EditarUsuario(LoginRequiredMixin,UpdateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuarios/editar_usuario.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje =f'{self.model.__name__} actualizado correctamente'
                error = 'No hay error'
                response = JsonResponse({'mensaje':mensaje, 'error':error})
                response.status_code = 201
                return response
            else:
                mensaje =f'{self.model.__name__} no se ha podido actualizar'
                error = form.errors
                response = JsonResponse({'mensaje':mensaje, 'error':error})
                response.status_code = 400
                return response
        else:
            return redirect('usuarios:Inicio_usuario')


class EliminarUsuario(LoginRequiredMixin,DeleteView):
    model = Usuario
    template_name = 'usuarios/eliminar_usuario.html'

    def delete(self, request, *args, **kwargs):
        if request.is_ajax():

            usuario = self.get_object()
            usuario.usuario_activo = False;
            usuario.save();
            mensaje =f'{self.model.__name__} eliminado  correctamente'
            error = 'No hay error'
            response = JsonResponse({'mensaje':mensaje, 'error':error})
            response.status_code = 201
            return response
            
        else:
            return redirect('usuarios:Inicio_usuario')