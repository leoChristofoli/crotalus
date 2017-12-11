from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy, reverse

from .forms import MessageForm
from .models import Message

def contact_view(request, email=None):
    try:
        print(request.POST['pre_email'])
    except:
        pass
    print('contact')
    for i in Message.objects.all():
        print(i.email, i.message)
    form = MessageForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        print(obj)
        obj.save()
        return HttpResponseRedirect(reverse('contact:home'))

    context = {
        'email': pre_email
    }
    template_name = 'contact/contact.html'

    return render(request, template_name, context)
