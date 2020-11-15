from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Empresa
from django.http import HttpResponse


# Create your views here.
class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome']

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return HttpResponse('OK')