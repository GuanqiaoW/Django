from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    # store infomation
    url(r'^store_view/$', views.viewStore, name='viewStore'),
    url(r'^add_store/$', views.addStore, name='addStore'),
    url(r'^store_view/(?P<id>\d+)/update/$', views.updateStore, name='updateStore'),
    # staff information
    url(r'^create_staff/$', views.createstaff, name='createstaff'),
    url(r'^staff_view/$', views.staffview, name='staffview'),
    url(r'^staff_view/(?P<id>\d+)/update/$', views.updatestaff, name='updatestaff'),
    # sale information
    url(r'^create_sale/$', views.createsale, name='createsale'),
    url(r'^sale_view/$', views.saleview, name='saleview'),
    url(r'^sale_view/(?P<id>\d+)/update/$', views.updatesale, name='updatesale'),
    #product infomation
    url(r'^create_product/$', views.createproduct, name='createproduct'),
    url(r'^product_view/$', views.productview, name='productview'),
    url(r'^product_view/(?P<id>\d+)/update/$', views.updateproduct, name='updateproduct'),
    # customer information
    url(r'^create_customer/$', views.createcustomer, name='createcustomer'),
    url(r'^customer_view/$', views.customerview, name='customerview'),
    url(r'^customer_view/(?P<id>\d+)/update/$', views.updatecustomer, name='updatecustomer'),
    # successful information page
    url(r'^thanks/$', views.thanks, name='thanks'),
    # login,logout,register
    url(r'^login/$', views.login_view, name='login_view'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^userprofile/$', views.userprofile_view, name='userprofile_view'),
    url(r'^userprofile/(?P<id>\d+)/update/$', views.updateprofile, name='updateprofile'),
    url(r'^register/$', views.register_view, name='register_view'),



    # url(r'^/register/$', views.register_view, name='register_view'),







]