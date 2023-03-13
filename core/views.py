from django.shortcuts import render, redirect, get_object_or_404 
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from .models import Item, OrderItem, Order, BillingAddress
from django.views.generic import TemplateView, ListView, View
#from .forms import visitorMessageForm, NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.utils import timezone
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    cakes = Item.objects.filter(category__name = 'Cakes')
    items = Item.objects.all()
    return render(request, 'index.html', {'cakes':cakes, 'items':items})


class shopView(ListView):
    model = Item 
    template_name = 'shop.html'

def shop_stands(request):
    stands = Item.objects.filter(category__name="Stands")
    return render(request, 'shop.html', {'stands':stands})

def shop_cakes(request):
    cakes = Item.objects.filter(category__name="Cakes")
    return render(request, 'shop.html', {'cakes':cakes})

def shop_decoration(request):
    decorations = Item.objects.filter(category__name="Decorations")
    return render(request, 'shop.html', {'decorations':decorations})

def shop_decorateTools(request):
    decorating_tools = Item.objects.filter(category__name="Decorating Tools")
    return render(request, 'shop.html', {'decorating_tools':decorating_tools}) 

def shop_bakeMat(request):
    bake_materials = Item.objects.filter(category__name="Baking Materials")
    return render(request, 'shop.html', {'bake_materials':bake_materials}) 

def shop_packageMat(request):
    package_materials = Item.objects.filter(category__name="Packaging Materials")
    return render(request, 'shop.html', {'package_materials':package_materials})

def checkout(request):
    return render(request, 'checkout.html', {}) 


def product_details(request, slug):
    item = Item.objects.get(slug=slug)
    similar = Item.objects.filter(category__name=item.category.name).exclude(slug=slug)
    return render(request, 'show_item.html', {'item':item, 'similar':similar})

def cakes(request):
    cakes = Item.objects.filter(category__name = 'Cakes')
    return render(request, 'cake.html', {'cakes':cakes}) 

def birthdayCake(request):
    birthday_cakes = Item.objects.filter(title__contains = 'birthday cake')
    return render(request, 'cake.html', {'birthday_cakes':birthday_cakes}) 

def weddingCake(request):
    wedding_cakes = Item.objects.filter(title__contains = 'wedding cake')
    return render(request, 'cake.html', {'wedding_cakes':wedding_cakes}) 

def searchShop(request):
    if request.method == 'POST':
        shopSearch = request.POST.get('shopSearch', False)
        shopResults = Item.objects.filter(title__contains=shopSearch)
        return render(request, 'shop.html', {'shopSearch':shopSearch, 'shopResults':shopResults}) 

def blog(request):
    return render(request, 'blog.html', {}) 

def menu(request):
    return render(request, 'menu.html', {}) 

def about_us(request):
    return render(request, 'about-us.html', {}) 

def contact(request):
    return render(request, 'contact.html', {}) 


class OrderSummary(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order=Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object':order
            }
            return render(self.request, 'cart.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You don't have an active order")
            return redirect("/")


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item = item, 
        user = request.user,
        ordered = False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        #check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity has been updated")
        else:
            messages.info(request, "This item was added to your cart")
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart")
    return redirect('cart')
    

def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    #fetch the user's order
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order=order_qs[0]
        #check if the order item exists or is in the order 
        if order.items.filter(item__slug=item.slug).exists():
            order_item=OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            messages.info(request, "This item was removed from your cart")
            return redirect('cart')
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("product-details", slug=slug)
    else:
        messages.info(request, "You don't have an active order")
        return redirect("product-details", slug=slug)
    return redirect("product-details", slug=slug)


def login(request):
    return render(request, 'faq.html', {})