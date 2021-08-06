from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Service, Employee
from .forms import ContactForm

# Create your views here.
class IndexView(FormView):
  template_name = 'index.html'
  form_class = ContactForm
  success_url = reverse_lazy('index')

  def get_context_data(self, **kwargs):
    context = super(IndexView, self).get_context_data(**kwargs)
    context['services'] = Service.objects.order_by('?').all()
    context['employees'] = Employee.objects.order_by('?').all()
    return context

  def form_valid(self, form, *args, **kwargs):
    form.send_mail()
    messages.success(self.request, 'Mail sended with succes')
    return super(IndexView, self).form_valid(form, *args, **kwargs)
  
  def form_invalid(self, form, *args, **kwargs):
    messages.error(self.request, 'Form is invalid')
    return super(IndexView, self).form_invalid(form, *args, **kwargs)