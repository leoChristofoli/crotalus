from django.conf.urls import url
from django.views.generic import TemplateView

from . import views as contact_views

urlpatterns = [
    url(
        regex=r'^$',
        view=contact_views.contact_view,
        name='home'
        ),

    url(
        regex=r'^thankyou/$',
        view=TemplateView.as_view(template_name='contact/thankyou.html'),
        name='thankyou'
        ),

]
