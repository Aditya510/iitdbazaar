from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Product
from django.http import HttpResponseRedirect
from .forms import QueryForm




def home(request):
    context = {
        'Products' : Product.objects.all()
    }
    return render(request, 'shop/home.html', context)

class ProductListView(ListView):
    model = Product
    template_name = 'shop/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'Products'
    ordering = ['-date_posted']
    paginate_by = 5


class UserProductListView(ListView):
    model = Product
    template_name = 'shop/user_Products.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'Products'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Product.objects.filter(seller=user).order_by('-date_posted')


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['title', 'description','content','price','image']
    success_url = '/'
    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['title', 'description','content','price','image']
    success_url = '/'
    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Product = self.get_object()
        if self.request.user == Product.seller:
            return True
        return False


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = '/'

    def test_func(self):
        Product = self.get_object()
        if self.request.user == Product.seller:
            return True
        return False


def about(request):
    return render(request, 'shop/about.html', {'title': 'About'})


def thanks(request):
    return render(request, 'shop/thanks.html', {'title': 'Thanks'})




def get_query(request, pk):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = QueryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            subject = "New Query from " + request.user.username + '!'
            query = form.cleaned_data.get('query')
            Product.objects.filter(pk=pk).first().seller.email_user(subject,query)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('../thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = QueryForm()

    return render(request, 'shop/sendquery.html', {'form': form})