from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import TodoModel
from django.urls import reverse_lazy

# Create your views here.

class List(ListView):
    template_name = 'list.html'
    model = TodoModel

class Detail(DetailView):
    template_name = 'details.html'
    model = TodoModel

class Create(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedatetime')
    success_url = reverse_lazy('list')

class Delete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')

class Update(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedatetime')
    success_url = reverse_lazy('list')

