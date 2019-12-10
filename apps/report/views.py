from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.shortcuts import render,redirect
from django.http import Http404
from django.urls import reverse

from apps.report.models import Report
from apps.post.models import Post
from . import app_conf

# Create your views here.

@login_required
def report_post(request,slug = None):
	if not slug is None and request.POST.get('report_radio'):
		try:
			current_user = get_user_model().objects.get(id=request.user.id)
		except get_user_model().DoesNotExist:
			pass
		post = get_object_or_404(Post,slug = slug)
		radio_value = int(request.POST.get('report_radio'))

		status = None
		if radio_value == 1:
			status = app_conf.SPAM
		elif radio_value == 2:
			status = app_conf.INAPPROPAITE
		elif radio_value == 3:
			status = app_conf.FALSE_INFO
		qry = Report.objects.filter(user=current_user,post=post)
		if not qry.exists():
			report_obj = Report(user = current_user,
								post = post,
								status = status)
			report_obj.save()
	return redirect(reverse('post:post-view',kwargs={'slug':slug}))