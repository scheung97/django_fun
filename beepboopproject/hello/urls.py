from django.urls import path
from .views import main
urlpatterns = [
    path('', main) #renders main from hello.views
]
