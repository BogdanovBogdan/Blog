from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q

from .models import *
from .utils import *
from .forms import *

def posts_list(request):
	search_request = request.GET.get('search', '')

	if search_request:
		posts = Post.objects.filter(Q(slug__icontains=search_request) | Q(body__icontains=search_request))
	else:
		posts = Post.objects.all()
	
	paginator = Paginator(posts, 3)
	page = paginator.get_page(request.GET.get('page'))
	

	return render(request, 'appblog/posts_list.html', context={'page': page})


def tags_list(request):
	tags = Tag.objects.all()
	return render(request, 'appblog/tags_list.html', context={'tags': tags})


class PostDetail(ObjectDetailMixin, View):
	model = Post
	template = 'appblog/post_detail.html'


class TagDetail(ObjectDetailMixin, View):
	model = Tag
	template = 'appblog/tag_detail.html'


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
	form = TagForm
	template = 'appblog/tag_create.html'
	raise_exception = True


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
	form = PostForm
	template = 'appblog/post_create.html'
	raise_exception = True


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
	model = Post
	form = PostForm
	template = 'appblog/post_update.html'
	raise_exception = True

	
class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
	model = Tag
	form = TagForm
	template = 'appblog/tag_update.html'
	raise_exception = True


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
	model = Post
	template = 'appblog/post_delete.html'
	redirect_url = 'posts_list'
	raise_exception = True


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
	model = Tag
	template = 'appblog/tag_delete.html'
	redirect_url = 'tags_list_url'
	raise_exception = True


	

	




