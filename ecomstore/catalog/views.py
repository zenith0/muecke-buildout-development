# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from models import Category, Product


def index(request, template_name="templates/catalog/index.html"):
    page_title = 'WebShop Products'
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))

## view for category
def show_category(request, category_slug, template_name="templates/catalog/category.html"):
    c = get_object_or_404(Category, slug=category_slug)
    products = c.product_set.all()
    page_title = c.name
    meta_keywords = c.meta_keywords
    meta_description = c.meta_description
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))

## view for product
def show_product(request, product_slug, template_name="templates/catalog/product.html"):
    p = get_object_or_404(Product, slug=product_slug)
    categories = p.categories.filter(is_active=True)
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))