
from book.models import Book,BookModel,BookOrderSearch
from django.forms import ModelForm

class NameForm(ModelForm):
	class Meta:
		model = BookModel
		fields ='__all__'


class BookOrderSearchForm(ModelForm):
	class Meta:
		model = BookOrderSearch
		fields = '__all__'