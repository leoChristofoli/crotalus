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
        regex=r'^(?P<email>[\w.@+-]+)/$',
        view=contact_views.contact_view,
        name='with-email'
    ),

]
