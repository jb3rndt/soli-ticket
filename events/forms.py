from django import forms
from django.forms import formset_factory

from .models import Event, Address, Buyable

class AddressForm(forms.ModelForm):
	# country = forms.CharField(required=False)
	# city = forms.CharField(required=False)
	# street = forms.CharField(required=False)
	# house_number = forms.CharField(required=False)
	# post_code = forms.DecimalField(required=False)
	class Meta:
		model = Address
		fields = [
			'country',
			'city',
			'street',
			'house_number',
			'post_code',
		]

class BuyableForm(forms.ModelForm):
	name = forms.CharField(required=True)
	price = forms.DecimalField(required=True)
	class Meta:
		model = Buyable
		fields = [
			'name',
			'price',
		]

BuyableFormSet = formset_factory(BuyableForm, extra=1)

class EventForm(forms.ModelForm):
	# address = AddressForm()
	# buyables = forms.ModelMultipleChoiceField(widget = forms.CheckboxSelectMultiple, queryset = Buyable.objects.all().values_list('name'))
	class Meta:
		model = Event
		fields = [
			'name',
			'description',
			'date',
			# 'address',
			# 'buyables',
		]