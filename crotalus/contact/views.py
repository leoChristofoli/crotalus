from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy, reverse

from .forms import MessageForm

def contact_view(request, email=None):
    print(email)
    form = MessageForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        print(obj)
        obj.save()
        return HttpResponseRedirect(reverse('contact:home'))

    context = {
        'email': email
    }
    template_name = 'contact/contact.html'

    return render(request, template_name, context)
