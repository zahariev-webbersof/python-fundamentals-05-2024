from django.urls import path

from djangoproject.phonebook.views import landing_page, create_contact

urlpatterns = [
    path('', landing_page, name='landing-page'),
    path('new_contact', create_contact, name='new-contact')
]