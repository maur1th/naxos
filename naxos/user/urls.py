from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy

from . import views


urlpatterns = patterns(
    '',
    url(
        regex=r'^$',
        view=views.UpdateUser.as_view(),
        name='profile'
    ),
    url(
        regex=r'^password/$',
        view=views.UpdatePassword,
        name='password'
    ),
    url(
        regex=r'^members/$',
        view=views.MemberList.as_view(),
        name='members'
    ),
    url(
        regex=r'^register/$',
        view=views.Register.as_view(),
        name='register'
    ),
    url(
        regex=r'^login/$',
        view=views.Login.as_view(),
        name='login'
    ),
    url(
        regex=r'^logout/$',
        view='django.contrib.auth.views.logout',
        kwargs={'next_page': reverse_lazy('user:login')},
        name='logout'
    ),
    url(
        regex=r'^node_api/$',
        view=views.node_api,
        name='node_api'
    ),
)
