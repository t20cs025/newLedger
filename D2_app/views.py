# Create your views here.
from .models import Ledger
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
# from .forms import ItemBuy, ItemIdForm, ItemForm
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from multiprocessing.sharedctypes import template
from django.contrib.gis.db.backends.spatialite import client
from django.urls.base import reverse_lazy
from django.views.generic.list import ListView


class Ledger(ListView):
    model = Ledger
    template_name='D2_app/list.html'

class MainView(TemplateView):
    template_name = 'D2_app/main.html'
    success_url = reverse_lazy('list')
     
class LoginView(TemplateView):
    template_name ='D2_app/login.html'
 
class SignUpView(TemplateView):
    template_name ='D2_app/signup.html'
     
class RegisterView(CreateView):
    model = Ledger
    fields = ('category','input_date','client','consumptionTax','excludingTax','includingTax')
    template_name = 'D2_app/register.html'
    success_url = 'list/'    
 
class ApprovalView(UpdateView):
    model = Ledger
    fields = ('category','input_date','client','consumptionTax_rate','consumptionTax','excludingTax','includingTax')
# #     context['category'] = CategoryForm()
    template_name = 'D2_app/approval.html'
    success_url = reverse_lazy('ledger_list')
# #     success_url = 'list/'    
class LedgerList(ListView):
    model = Ledger
    template_name = 'D2_app/ledger.html'
     
class DocumentView(TemplateView):
    template_name ='D2_app/document.html'