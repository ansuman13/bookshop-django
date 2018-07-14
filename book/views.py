from django.shortcuts import render,reverse,redirect
from django.views.generic import TemplateView,ListView,DetailView,UpdateView
from .models import BookModel,BookOrderSearch,VisionBooksModel
from .forms import NameForm,BookOrderSearchForm
from django.http import HttpResponse
from isbnlib import meta,desc,cover
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from cart.cart import Cart
# Create your views here.
from pprint import pprint
from bs4 import BeautifulSoup
import requests

# def search(request):
# 	q = request.GET.get('q')

# 	if q:
# 		books = BookDocument.search().query("match",title=q)
# 	else:
# 		books = ''
# 	return render(request,'search.html',{'books':books})
	
	
class IndexView(ListView):
	model = BookModel

class VisionBooksViews(ListView):
	model = VisionBooksModel

class BookDetailView(DetailView):
	model =BookModel

class BookUpdateView(LoginRequiredMixin, UpdateView):
	model = BookModel
	fields ='__all__'

def search_order(request):
	if request.method == 'POST':
		form = BookOrderSearchForm(request.POST)
		if form.is_valid():
			title = str(form.cleaned_data['title'])
			keyword = str(form.cleaned_data['keyword'])
			author = str(form.cleaned_data['author'])
			isbn = str(form.cleaned_data['isbn'])
			userquery = 'test'
			userinput = []
			userinput.append(title)
			userinput.append(keyword)
			userinput.append(author)
			userinput.append(isbn)
			print(userinput)
			for item in userinput:
				if item != '' and item != "None":
					print(item)
					userquery = item
			userquery = userquery.replace(" ","+")
			url = "https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Dstripbooks&field-keywords="+str(userquery)
			# url = 'https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Dstripbooks&field-keywords=to+kill+a+mocking+bird&rh=n%3A976389031%2Ck%3Ato+kill+a+mocking+bird'
			response = requests.get(url, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'})
			soup = BeautifulSoup(response.content,'lxml')
			# print(soup.prettify())
			result=soup.find('ul',id='s-results-list-atf')
			print(url)
			return HttpResponse(result)
	else:
		form = BookOrderSearchForm()
	return render(request,'order.html',{'form':form})
		

@login_required
def get_name(request):
	if request.method=='POST':
		form = NameForm(request.POST)
		if form.is_valid():
			isbn=str(form.cleaned_data['isbn'])
			SERVICE = 'default'
			my_dict = meta(isbn,SERVICE)
			print(my_dict)
			obj = form.save(commit=False)
			if (desc(isbn)) is None:
				pass
			else:
				my_dict['desc'] = (desc(isbn))
				obj.desc= my_dict['desc']	
			if (cover(isbn)) is None:
				pass
			else:
				my_dict['covers'] = (cover(isbn))
				obj.thumbnail_small= my_dict['covers']['smallThumbnail']
				obj.thumbnail= my_dict['covers']['thumbnail']
				
			obj.isbn= my_dict['ISBN-13']
			obj.title= my_dict['Title']
			obj.authors= my_dict['Authors'][0]
			obj.publisher= my_dict['Publisher']
			obj.year= my_dict['Year']				
			obj.save()
			return redirect("book:index")
	else:
		form =NameForm()
	return render(request,'name.html',{'form':form})

def add_to_cart(request,isbn):
	print('method get')
	print(isbn)
	product = BookModel.objects.get(isbn=isbn)
	cart=Cart(request)
	cart.add(product,product.prices,product.quantity)
	return redirect("/site")

def remove_from_cart(request,isbn):
    product = BookModel.objects.get(isbn=isbn)
    cart = Cart(request)
    cart.remove(product)

def view_cart(request):
    return render(request,'cart.html', dict(cart=Cart(request)))
# def add_to_cart(request, product_id, quantity):
#     product = Product.objects.get(id=product_id)
#     cart = Cart(request)
#     cart.add(product, product.unit_price, quantity)
