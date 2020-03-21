from django.shortcuts import render, redirect

from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from .models import *
from .forms import PacienteForm


# Create your views here.

class CnvView(generic.ListView):
	model = Paciente
	template_name = "cnv/cnv_list.html"
	context_object_name = "obj"

class CnvNew(generic.CreateView):
	model = Paciente
	form_class = PacienteForm
	template_name = "cnv/cnv_form.html"
	success_url = reverse_lazy('cnv/cnv_list')
	
	

	
	