from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('contact_details/<id>',views.contact_details,name="contact_details"),
    path('delete_contact/<id>',views.delete_contact,name="delete_contact"),
    path('edit_contact/<id>',views.edit_contact,name="edit_contact"),
    # path('populate',views.populate_contacts,name="populate_contact"),
]
