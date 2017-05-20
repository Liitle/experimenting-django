from django.conf.urls import url

from . import views

urlpatterns = [
    # /dashboard/
    url(r'^$', views.index, name='index'),

    # /dashboard/expense_id
    url(r'^(?P<expense_id>[0-9]+)/$', views.detail, name='detail')
]
