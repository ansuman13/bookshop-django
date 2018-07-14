from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.conf import settings
app_name = 'book'

urlpatterns = [
	url(r'^site$',views.IndexView.as_view(),name='index'),
	url(r'^name$',views.get_name,name='get_name'),
	url(r'^order$',views.search_order,name='order'),
	url(r'^detail/(?P<pk>\d+)$',views.BookDetailView.as_view(),name='book_details'),
	url(r'^update/(?P<pk>\d+)$',views.BookUpdateView.as_view(success_url='/name'),name='book_update'),
	url(r'^cart/(?P<isbn>\d+)/$',views.add_to_cart, name='add_to_cart'),
	url(r'^rcart/(?P<isbn2>\d+)/$',views.remove_from_cart ,name='remove_from_cart'),
	url(r'^cart/$',views.view_cart,name='view_cart'),
	url(r'^all/$',views.VisionBooksViews.as_view(),name='all'),
	# url(r'^detail/$',views.cartme,name='cartme'),	
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)