from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import *

class ObjectDetailMixin:
	model = None
	template = None

	def get(self, request, slug):
		obj = get_object_or_404(self.model, slug__iexact=slug)
		return render(request, self.template, context={self.model.__name__.lower(): obj, 'admin_panel': obj, 'detail': True})


class ObjectCreateMixin:
	form = None
	template = None

	def get(self, request):
		return render(request, self.template, context={'form': self.form()})

	def post(self, request):
		bound_form = self.form(request.POST)
		
		if bound_form.is_valid():
			return redirect(bound_form.save())
			
		return render(request, self.template, context={'form': bound_form})


class ObjectUpdateMixin:
	model = None
	form = None
	template = None

	def get(self, request, slug):
		obj = self.model.objects.get(slug__iexact=slug)
		bound_form = self.form(instance=obj)
		return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

	def post(self, request, slug):
		obj = self.model.objects.get(slug__iexact=slug)
		bound_form = self.form(request.POST, instance=obj)

		if bound_form.is_valid():
			update_post = bound_form.save()
			return redirect(update_post)
		return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})


class ObjectDeleteMixin:
	model = None
	template = None
	redirect_url = None

	def get(self, request, slug):
		obj = self.model.objects.get(slug__iexact=slug)
		return render(request, self.template, context={self.model.__name__.lower(): obj})

	def post(self, request, slug):
		obj = self.model.objects.get(slug__iexact=slug)
		obj.delete()
		return redirect(reverse(self.redirect_url))
