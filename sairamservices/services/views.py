from django.shortcuts import render
from django.views.generic import TemplateView, View, DetailView
from django.http import HttpResponseRedirect
from .forms import EnquiryForm
from .models import *
from .utils import send_email_to_admin
# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['slider'] = Slider.objects.all()
        context['slider_list'] = range(len(context['slider']))
        context['about_us_slider_list'] = AboutUs.objects.all()[:3]
        context['about_us'] = AboutUs.objects.all()[3:4]
        context['why_us'] = WhyUs.objects.all()
        context['services'] = Service.objects.all()
        context['contact'] = ContactUs.objects.all()
        context['settings'] = Settings.objects.all()
        context['form'] = EnquiryForm()
        context['url'] = ""
        return context

class AboutUSView(TemplateView):
    template_name = "about_us.html"

    def get_context_data(self, **kwargs):
        context = super(AboutUSView, self).get_context_data(**kwargs)
        context['contact'] = ContactUs.objects.all()
        context['settings'] = Settings.objects.all()
        context['about_us'] = AboutUs.objects.all()[3:]
        context['form'] = EnquiryForm()
        context['url'] = "about"
        return context

class WhyView(TemplateView):
    template_name = "why.html"

    def get_context_data(self, **kwargs):
        context = super(WhyView, self).get_context_data(**kwargs)
        context['why_slider'] = AboutUs.objects.all()[:3]
        context['why_us'] = WhyUs.objects.all()
        context['contact'] = ContactUs.objects.all()
        context['settings'] = Settings.objects.all()
        context['form'] = EnquiryForm()
        context['url'] = "why"
        return context

class ServiceView(TemplateView):
    template_name = "service.html"

    def get_context_data(self, **kwargs):
        context = super(ServiceView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        context['contact'] = ContactUs.objects.all()
        context['settings'] = Settings.objects.all()
        context['form'] = EnquiryForm()
        context['url'] = "services"
        return context

class ContactView(TemplateView):
    template_name = "contact_us.html"

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['contact'] = ContactUs.objects.all()
        context['settings'] = Settings.objects.all()
        context['form'] = EnquiryForm()
        context['url'] = "contact"
        return context

class EnquiryView(View):

    def post(self, request):
        ctx = {
            'name':self.request.POST.get('name'),
            'phone_number': self.request.POST.get('contact_no'),
            'email': self.request.POST.get('email'),
            'address': self.request.POST.get('address'),
            'product': self.request.POST.get('product'),
            'brand': self.request.POST.get('brand'),
            'service': self.request.POST.get('service'),
            'message': self.request.POST.get('message')
        }
        url = self.request.POST.get('url')
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
        send_email_to_admin(ctx)
        return HttpResponseRedirect(url)

class DetailsView(DetailView):
    models = Service
    template_name = "details.html"

    def get_context_data(self, **kwargs):
        context = super(DetailsView, self).get_context_data(**kwargs)
        context['contact'] = ContactUs.objects.all()
        context['settings'] = Settings.objects.all()
        context['details'] = Service.objects.get(pk=self.kwargs.get("key_id"))
        context['form'] = EnquiryForm()
        return context

    def get_object(self, queryset=None):
        return Service.objects.get(pk=self.kwargs.get("key_id"))
