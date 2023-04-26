from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from .models import *
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'website/index.html', {})


def about(request):
    return render(request, 'website/about.html', {})


def gallery(request):
    return render(request, 'website/gallery.html', {})


def categories(request):
    data = Category.objects.all().order_by('-id')
    return render(request, 'website/categories.html', {'data': data})


def all_products(request):
    data = Product.objects.all().order_by('id')
    cats = Product.objects.distinct().values('category__title')
    sizes = ProductAttribute.objects.distinct().values('size__title')
    return render(request, 'website/all_products.html',
                  {
                      'data':data,
                      'cats':cats,
                      'sizes': sizes,
                  }
                  )


def category_product_list(request,cat_id):
    category=Category.objects.get(id=cat_id)
    data=Product.objects.filter(category=category).order_by('id')
    cats = Product.objects.distinct().values('category__title')
    sizes = ProductAttribute.objects.distinct().values('size__title')
    return render(request, 'website/category_product_list.html',
                  {
                      'data': data,
                      'cats': cats,
                      'sizes': sizes,
                  }
                  )

@login_required(login_url='login')
def product_detail(request, slug, id):
    product=Product.objects.get(id=id)
    sizes = ProductAttribute.objects.filter(product=product).values('size__id', 'size__title', 'price',).distinct()

    return render(request, 'website/product_detail.html',
                  {'data': product, 'sizes': sizes,})


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created for ' + user)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'website/register.html', {'form': form})


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            #include flash message in case of invalid login credentials
            messages.error(request, 'Invalid username or password.')
            return render(request, 'website/login.html')
    else:
        return render(request, 'website/login.html', {})


def logoutUser(request):
    logout(request)
    return redirect('website/login')


def filter_data(request):
    categories = request.GET.getlist('category[]')
    sizes = request.GET.getlist('size[]')
    allProducts = Product.objects.all().order_by('-id').distinct()
    if len(categories) > 0:
        allProducts = allProducts.filter(category__id__in=categories).distinct()
    if len(categories) > 0:
        allProducts = allProducts.filter(productattribute__size__id__in=sizes).distinct()
    t = render_to_string('website/all_products.html', {'data': allProducts})
    return JsonResponse({'data': t})


def search(request):
    q=request.GET['q']
    data=Product.objects.filter(title__icontains=q).order_by('id')
    return render(request, 'website/search.html', {'data': data})

