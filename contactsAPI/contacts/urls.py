

from .views import ContactList, ContactDetail
from django.urls import path

urlpatterns = [
    path('', ContactList.as_view()),
    path('<int:id>', ContactDetail.as_view()),
]
