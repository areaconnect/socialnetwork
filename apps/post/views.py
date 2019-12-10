from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from apps.common.decorators import ajax_required
from django.contrib.auth import get_user_model
from django.shortcuts import render,redirect
from django.http import Http404
from django.urls import reverse

from apps.post.models import Post
from apps.activity import utils



@ajax_required
@login_required
@require_http_methods(["POST"])
def post_like_unlike(request):
	user = request.user
	post_id = request.POST.get('post_id');
	post    = get_object_or_404(Post,id = post_id)
	is_liked = None
	if request.user in post.users_like.all():
		post.users_like.remove(request.user)
		is_liked = False
	else:
		is_liked = True
		post.users_like.add(request.user)
		utils.create_action(user,'likes',post)
	likes_count = post.likes_count
	return JsonResponse({'liked':is_liked,'likes_count':likes_count})



@login_required
def post_add(request):
	if request.method == 'POST' and request.FILES['file']:
		username = request.POST.get('post_owner')
		owner 	= get_object_or_404(get_user_model(),username__iexact=username.strip())
		title = request.POST.get('title')
		content = request.POST.get('content')
		file 	= request.FILES.get('file')
		# TODO : validate user input & files( size,format,dimensions,ip(optional))
		post_instance,_ = Post.objects.\
		get_or_create(owner = owner,
		title = title,
		content = content,
		photo = file)
		utils.create_action(owner,'added a new post',post_instance)
		return redirect(reverse('account:user-profile',kwargs={'username':owner.username}))
	else:
		pass



def viewed_by_session(request,post_obj):
	session_key = 'viewed_topic_{}'.format(post_obj.id)
	if not request.session.get(session_key,False):
		post_obj.views += 1
		post_obj.save()
		request.session[session_key] = True


def post_view(request,slug = None):
	if not slug is None:
		post_instance = get_object_or_404(Post,slug = slug.strip())
		viewed_by_session(request,post_instance)
		comments = post_instance.post_comments
	return render(request,'post/post_detail_view.html',
		{'post':post_instance,
		'comments':comments})



@login_required
def post_delete(request,slug):
	# only post owners and superusers or admin can delete post
	return HttpResponse(slug)