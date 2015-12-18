from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.upload_file_view, name='upload_file'),
    url(r'^get_parameters/$', views.get_parameters_view, name='get_parameters'),
    url(r'^download/$', views.download_file_view, name='download'),

    #
    # # LOGIN
    # # url(r'^login/$', views.login_view, name='login'),
    # url(r'^login/$', views.login_view),
    # url(r'^auth/$', views.auth_view),
    # url(r'^logout/$', views.logout_view),
    # url(r'^loggedin/$', views.loggedin_view),
    # # url(r'^invalid/$', views.invalid_login_view),
    #
    #
    # # REGISTRATION
    # url(r'^register/$', views.register_user_view),
    # url(r'^register_success/$', views.register_success_view),
    #
    # #GOAL CREATION
    # url(r'^add_goal/$', views.add_goal_view)
]