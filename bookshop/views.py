from django.views.generic import TemplateView
from django.shortcuts import render
class ThanksPage(TemplateView):
	template_name = 'thanks.html'

from cart.cart import Cart
from book.models import BookModel
