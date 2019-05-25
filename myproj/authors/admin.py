from django.contrib import admin
from authors.models import Author
# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('id', '__str__', 'email_address', 'email_domain', 'level')
	list_display_links = ('id', '__str__')

	empty_value_display = '<not stated>'

	def email_address(self, obj):
		if obj.email is not None:
			return obj.email

	def email_domain(self, obj):
		if obj.email is not None:
			return obj.email.partition('@')[2]

	email_address.empty_value_display = '<no email>'

# admin.site.register(Author, AuthorAdmin)
