from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *
from .utils import DataMixin
from django.contrib.auth import get_user_model, login, logout
from .forms import *
from django.contrib.auth.views import LoginView
from .utils import menu
from django.contrib.auth.mixins import LoginRequiredMixin


class ShopHome(DataMixin, ListView):
    model = ComputerElems
    template_name = 'shop/index.html'
    context_object_name = 'comp_elems'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cpu = ComputerElems.objects.filter(cat__name='CPU').order_by('-time_create')[:4]
        gpu = ComputerElems.objects.filter(cat__name='GPU').order_by('-time_create')[:4]
        motherboard = ComputerElems.objects.filter(cat__name='Motherboard').order_by('-time_create')[:4]
        ram = ComputerElems.objects.filter(cat__name='RAM').order_by('-time_create')[:4]
        discs = ComputerElems.objects.filter(cat__name='SSD/HHD/discs').order_by('-time_create')[:4]
        cooling = ComputerElems.objects.filter(cat__name='Cooling').order_by('-time_create')[:4]
        power_supply = ComputerElems.objects.filter(cat__name='Power supply').order_by('-time_create')[:4]
        case = ComputerElems.objects.filter(cat__name='Case').order_by('-time_create')[:4]
        total_comp = ComputerElems.objects.all().count()
        User = get_user_model()
        users = User.objects.all().count()
        c_def = self.get_user_content(title='HOME', cpu=cpu, gpu=gpu, motherboard=motherboard, ram=ram, discs=discs, cooling=cooling, power_supply=power_supply, case=case, total=total_comp, users=users)
        return dict(list(context.items()) + list(c_def.items()))


class ShopShop(DataMixin, ListView):
    model = ComputerElems
    template_name = 'shop/shop.html'
    context_object_name = 'shop'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title='SHOP')
        return dict(list(context.items()) + list(c_def.items()))


class ShowCompElem(DataMixin, DetailView):
    model = ComputerElems
    template_name = 'shop/comp_elem.html'
    slug_url_kwarg = 'post_elem_slug'
    context_object_name = 'component'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title=context['component'])
        return dict(list(context.items()) + list(c_def.items()))


class ShowCatCompElem(DataMixin, ListView):
    model = ComputerElems
    template_name = 'shop/shop.html'
    context_object_name = 'shop'
    allow_empty = False

    def get_queryset(self):
        return ComputerElems.objects.filter(cat__slug=self.kwargs['cat_elem_slug'], available=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = CatComputerElems.objects.get(slug=self.kwargs['cat_elem_slug'])
        c_def = self.get_user_content(title='Category - ' + str(categories.name), cat_selected=categories.pk)
        return dict(list(context.items()) + list(c_def.items()))


def ShopAboutUs(request):
    context = {
        'title': 'ABOUT US',
        'total': ComputerElems.objects.all().count(),
        'users': User.objects.all().count(),
        'menu': menu
    }

    return render(request, 'shop/about_us.html', context)


class ShopContact(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'shop/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title='CONTACT')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return render('home')


class ShopAddElem(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddElem
    template_name = 'shop/add_elem.html'
    context_object_name = 'form'
    success_url = reverse_lazy('shop')
    login_url = reverse_lazy('login')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title='ADD ELEMENT')
        return dict(list(context.items()) + list(c_def.items()))


class ShopRegister(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'shop/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title='REGISTER')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


class ShopLogin(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'shop/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title='LOGIN')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

    def set_session(self):
        if self.request.method == 'POST' and ('user_id' not in self.request.session):
            user = User.objects.get(username=self.request.POST['username'])
            if user.check_password(self.request.POST['password']):
                self.request.session.set_expiry(60)
                self.request.session['user_id'] = user.id
                return reverse_lazy('home')
            else:
                return redirect('login')


def ShopLogout(request):
    logout(request)
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return redirect('login')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Strona nie znaleziona</h1>')

