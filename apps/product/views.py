from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, FormView

from apps.product.forms import *
from apps.product.models import *


class CreateCategory(CreateView):
    model = Category
    form_class = CreateCategoryForm
    template_name = 'product/create_category.html'
    success_url = reverse_lazy('index:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_categories'] = Category.objects.all()
        return context


class ShowCategoryListAdmin(ListView, FormView):
    model = Category
    template_name = 'product/show_category_list_admin.html'

    success_url = reverse_lazy('product:show_categories_list_admin')
    form_class = CategoryListAdminForm

    def form_valid(self, form):
        Category.objects.filter(id=form.cleaned_data['category_id']).delete()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_categories'] = Category.objects.all()
        return context


class CreateProduct(CreateView):
    model = Product
    success_url = reverse_lazy('index:index')
    form_class = CreateProductForm
    template_name = 'product/create_product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        context['category'] = category
        kwargs['category'] = category
        print(category.name)
        context['product_categories'] = Category.objects.all()
        return context

    def form_valid(self, form):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        form.instance.category = category
        return super().form_valid(form)
