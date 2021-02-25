from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Provider


class ProviderListView(LoginRequiredMixin, generic.ListView):
    template_name = 'providers/provider_list.html'

    def get_queryset(self):
        return Provider.objects.all()
