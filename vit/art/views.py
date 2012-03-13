import time
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.context_processors import csrf
from django.shortcuts import get_object_or_404, render_to_response
from django.forms import ModelForm
from vit.art.models import *
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from vit.art.forms import *
from django.utils import simplejson
from django.core import serializers
from django.template import Context, loader

def post(request, pk):
  post = Post.objects.get(pk=int(pk))
  comments = Comment.objects.filter(post=post)
  d = dict(post=post, comments=comments, form=CommentForm(), user=request.user)
  d.update(csrf(request))
  cf_obj = Comment(post = Post.objects.get(pk=pk))
  if request.method == 'POST' and request.is_ajax():
    comment_form = CommentForm(request.POST, instance = cf_obj)
    if comment_form.is_valid():
      comment = comment_form.save(commit=True)
    else:
     raise Http404
    response = serializers.serialize('json', [comment])
    return HttpResponse(response, mimetype='application/json')
  return render_to_response("post.html", d)

def main(request):
  posts = Post.objects.all().order_by("-created")
  paginator = Paginator(posts, 5)
  try:  page = int(request.GET.get("page", '1'))
  except ValueError: page = 1
  try:
    posts = paginator.page(page)
  except (InvalidPage, EmptyPage):
    posts = paginator.page(paginator.num_pages)
  return render_to_response("main.html", dict(posts=posts, user=request.user,                               post_list=posts.object_list))

def index(request):
  latest_post_list = Post.objects.all().order_by('-created')
  return render_to_response('index.html',dict(latest_post_list=latest_post_list,user=request.user, post_list=latest_post_list))



