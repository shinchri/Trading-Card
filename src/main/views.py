from django.shortcuts import render
from django.views import generic

from .models import Product

# Create your views here.
class HomeView(generic.TemplateView):
  template_name = 'home.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    products = Product.objects.all()

    context["products"] = products

    return context

class ProductDetailView(generic.TemplateView):
  template_name = 'product-detail.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    
    product_id = self.kwargs.get('id')
    product = Product.objects.get(id=product_id)

    context['product'] = product
    
    return context