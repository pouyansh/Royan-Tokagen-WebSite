from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView

from apps.product.models import Product, Category
from apps.registration.models import Customer, Person, Organization
from apps.research.models import ResearchArea
from apps.service.models import Service, Field
from apps.tutorial.models import Tutorial


class StartOrderProduct(LoginRequiredMixin, TemplateView):
    template_name = "order_product/start_order.html"

    def dispatch(self, request, *args, **kwargs):
        if not Product.objects.filter(id=self.kwargs['pk']):
            return render(request, "temporary/show_text.html", {'text': "کالای مورد نظر یافت نشد"})
        if self.request.user.is_superuser:
            return render(request, "temporary/show_text.html", {'text': "ثبت سفارش مخصوص مشتریان است"})
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_categories'] = Category.objects.filter(is_active=True).order_by('id')
        context['services'] = Service.objects.all().order_by('id')
        context['service_fields'] = Field.objects.all().order_by('id')
        context['research_areas'] = ResearchArea.objects.all().order_by('id')
        context['tutorials'] = Tutorial.objects.all().order_by('id')
        customer = Customer.objects.get(username=self.request.user.username)
        context['logged_in_customer'] = customer
        if customer.is_person:
            context['logged_in_user'] = Person.objects.get(username=self.request.user.username)
        else:
            context['logged_in_user'] = Organization.objects.get(username=self.request.user.username)
        product = Product.objects.get(id=self.kwargs['pk'])
        context['product'] = product
        return context
