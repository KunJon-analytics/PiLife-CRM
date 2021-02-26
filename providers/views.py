from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from leads.models import Provider
from .forms import ProviderModelForm


class ProviderListView(LoginRequiredMixin, generic.ListView):
    template_name = 'providers/provider_list.html'

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Provider.objects.filter(organisation=organisation)

class ProviderCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'providers/provider_create.html'
    form_class = ProviderModelForm

    def get_success_url(self):
        return reverse("providers:provider-list")

    def form_valid(self, form):
        provider = form.save(commit=False)
        provider.organisation = self.request.user.userprofile
        provider.save()
        return super(ProviderCreateView, self).form_valid(form)

class ProviderDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'providers/provider_detail.html'
    context_object_name = "provider"

    def get_queryset(self):
        return Provider.objects.all()

class ProviderUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'providers/provider_update.html'
    form_class = ProviderModelForm

    def get_success_url(self):
        return reverse("providers:provider-list")

    def get_queryset(self):
        return Provider.objects.all()

class ProviderDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'providers/provider_delete.html'
    context_object_name = "provider"

    def get_success_url(self):
        return reverse("providers:provider-list")

    def get_queryset(self):
        return Provider.objects.all()