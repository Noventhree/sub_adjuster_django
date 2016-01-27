from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.upload_file_view, name='upload_file'),
    url(r'^get_parameters/$', views.get_parameters_view, name='get_parameters'),
    url(r'^confirm_adjustment/$', views.confirm_adjustment_view, name='confirm_adjustment'),
    # url(r'^download/$', views.download_file_view, name='adjust'),

]