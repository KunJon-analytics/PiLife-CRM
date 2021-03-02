import random

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import reverse
from leads.models import Provider
from .forms import ProviderModelForm
from .mixins import OrganiserAndLoginRequiredMixin


class ProviderListView(OrganiserAndLoginRequiredMixin, generic.ListView):
    template_name = 'providers/provider_list.html'

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Provider.objects.filter(organisation=organisation)


class ProviderCreateView(OrganiserAndLoginRequiredMixin, generic.CreateView):
    template_name = 'providers/provider_create.html'
    form_class = ProviderModelForm

    def get_success_url(self):
        return reverse("providers:provider-list")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_provider = True
        user.is_organiser = False
        user.set_password(f"{random.randint(0,1000000)}")
        user.save()
        Provider.objects.create(
            user=user,
            organisation=self.request.user.userprofile
        )
        send_mail(
            subject="You are invited to be a provider",
            message="You were added as a Provider on PiLife, Please come login to start working.",
            from_email="kunjonng@gmail.com",
            recipient_list=[user.email]
        )
        return super(ProviderCreateView, self).form_valid(form)


class ProviderDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'providers/provider_detail.html'
    context_object_name = "provider"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Provider.objects.filter(organisation=organisation)


class ProviderUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'providers/provider_update.html'
    form_class = ProviderModelForm

    def get_success_url(self):
        return reverse("providers:provider-list")

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Provider.objects.filter(organisation=organisation)


class ProviderDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'providers/provider_delete.html'
    context_object_name = "provider"

    def get_success_url(self):
        return reverse("providers:provider-list")

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Provider.objects.filter(organisation=organisation)
