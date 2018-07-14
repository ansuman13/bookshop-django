from django.contrib import admin
from .models import Book,BookModel,SubjectModel,VisionBooksModel
# Register your models here.

admin.site.register(Book)
admin.site.register(SubjectModel)
admin.site.register(BookModel)
admin.site.register(VisionBooksModel)
