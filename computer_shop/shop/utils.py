from .models import *
from django.db.models import *

menu = [{'title': 'home', 'url_name': 'home'},
        {'title': 'about us', 'url_name': 'about_us'},
        {'title': 'shop', 'url_name': 'shop'},
        {'title': 'contact', 'url_name': 'contact'}]


class DataMixin:
    paginate_by = 15
    def get_user_content(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        cat_comp_elems = CatComputerElems.objects.annotate(Count('computerelems'))
        context['category'] = cat_comp_elems
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context