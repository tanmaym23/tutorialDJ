# from django.conf.urls import url
from formsapp import views
from django.urls import path


# template tagging
app_name='formsapp'

urlpatterns = [
    path('forms',views.contact_view,name='forms'),
    path('other',views.other,name='other'),
]