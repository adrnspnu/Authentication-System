from django.urls import path
from . views import *
urlpatterns = [
    path("",index, name="kennyindex"), path("linkhello/",hello, name="hello"), path("linklogin/",login, name="login")

]
