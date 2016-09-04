from django.shortcuts import render, redirect
from django.http import JsonResponse

from models import Post
from forms import PostForm

from rest_framework.response import Response
from serializers import PostSerializer


INITIAL_COUNT = 20
LOAD_MORE_COUNT = 20

#API
def like_api(request):
  post_id = request.GET['id']
  post = Post.objects.get(pk=int(post_id))
  post.like = post.like + 1
  post.save()

  return JsonResponse({
    'code' : '100',
    'msg': 'success',
    })

#API
def load(request):
  count = int(request.GET['count'])
  mode = request.GET['mode']

  if mode == 'created_at':
    posts = Post.objects.order_by('-created_at')[count:LOAD_MORE_COUNT+count]
  else:
    posts = Post.objects.order_by('-like')[count:LOAD_MORE_COUNT+count]

  return JsonResponse({ 
    'code' : '100',
   'msg': 'success',
   'posts': PostSerializer(posts, many=True).data
   })


def index(request):
    mode = 'created_at'
    if 's' in request.GET:
      posts = Post.objects.order_by('-like')[:INITIAL_COUNT]
      mode = 'like'
    else:
      posts = Post.objects.order_by('-created_at')[:INITIAL_COUNT]
    data = {
      'posts': posts,
      'mode': mode,
      'form': PostForm()
    }
    return render(request, 'myapp/home.html', data)

def post(request):
    form = PostForm(data=request.POST)
    if form.is_valid():
      Post.objects.create(
        kakeru=form.cleaned_data['kakeru'],
        toku=form.cleaned_data['toku'],
        kokoro=form.cleaned_data['kokoro'],
      )
    return redirect(index)


def like(request):
    
    if request.method == 'POST':
      id = request.POST['id']
      post = Post.objects.get(pk=int(id))
      post.like = post.like + 1
      post.save()

    return redirect(index)