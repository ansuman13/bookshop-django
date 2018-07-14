"""bookshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'',include('book.urls',namespace='book')),
	url(r'^accounts/',include('accounts.urls',namespace='accounts')),
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.ThanksPage.as_view(),name='thanks'),
    # url(r'^cart/',views.get_cart,name='cart'),
    url(r'^search/',include(('haystack.urls','search'),namespace='search')),
]
