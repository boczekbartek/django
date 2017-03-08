from django.views import generic
from .models import Sauce, Pasta

class SauceView(generic.ListView):
    template_name = 'orders/sauce.html'
    context_object_name = 'all_sauces'

    def get_queryset(self):
        return Sauce.objects.all()

class PastaView(generic.ListView):
    template_name = 'orders/pasta.html'
    context_object_name = 'all_pastas'

    def get_queryset(self):
        return Pasta.objects.all()