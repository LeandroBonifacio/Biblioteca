from django.db import models
from django.db.models.base import Model
from django.http import request
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView
from .forms import AutorForm, LibroForm
from .models import Autor, Libro
from django.urls import reverse_lazy
"""
    dispatch(): valida la peticion y elige que metodo HTTP se utilizo para la solicitud
    http_method_not_allowed(): retorna un error cuando se utiliza un metodo HTTP no soportado o definido
    options(): 


    POP 257
    def get_queryset(self):
        #Retorna la consulta a utilizar en toda la clase
        return self.model.objects.filter(estado = True)
"""



class listadoAutor(ListView):
    models = Autor
    template_name = 'libro/autor/listar_autor.html'
    context_object_name = 'autores'
    queryset = Autor.objects.filter(estado=True)

class actualizarAutor(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'libro/autor/crear_autor.html'
    success_url = reverse_lazy('libro:listar_autor')

class crearAutor(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'libro/autor/crear_autor.html'
    success_url = reverse_lazy('libro:listar_autor')

class eliminarAutor(DeleteView):
    model = Autor
    def post(self, request, pk, *args, **kwargs):
        object = Autor.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('libro:listar_autor')


""" VISTAS BASADAS EN FUNCIONES
def crearAutor(request):
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        if  autor_form.is_valid():
            autor_form.save()
            return redirect('index')
    else:
        autor_form = AutorForm()
    return render(request, 'libro/crear_autor.html', {'autor_form': autor_form})


def listarAutor(request):
    autores = Autor.objects.filter(estado=True);
    return render(request, 'libro/listar_autor.html', {'autores': autores});

def editarAutor(request, id):
    autor_form = None;
    error = None;
    try:
        autor = Autor.objects.get(id = id);
        if  request.method == 'GET':
            autor_form = AutorForm(instance=autor)
        else:
            autor_form = AutorForm(request.POST, instance = autor)
            if  autor_form.is_valid():
                autor_form.save();
                redirect('libro:listar_autor')
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'libro/crear_autor.html', {'autor_form': autor_form, 'error': error})
    

def eliminarAutor(request, id):
    autor = Autor.objects.get(id = id);
    autor.estado = False
    autor.save()
    return redirect('libro:listar_autor')
"""

class ListadoLibros(View):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/listar_libro.html'

    def get_queryset(self):
        return self.model.objects.filter(estado = True)

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto ['libros'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())



class CrearLibro(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/crear_libro.html'
    success_url = reverse_lazy('libro:listado_libros')


class ActualizarLibro(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/modal_libro.html'
    success_url = reverse_lazy('libro:listado_libros')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['libros'] = Libro.objects.filter(estado = True)
        return context
        

class EliminarLibro(DeleteView):
    model = Libro
    def post(self, request, pk, *args, **kwargs):
        object = Libro.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('libro:listado_libros')