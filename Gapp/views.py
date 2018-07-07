from django.shortcuts import render
from Gapp import forms as G_forms
from django.http import JsonResponse,HttpResponse
from Gapp import models as G_models
import json
# Create your views here.

def home(request):
	a = G_models.Announcements.objects.all()
	return render(request,'Gapp/temps/home.html',{'home':'active','news':a})

# Article Function
def ArticleView(request):
	form_class = G_forms.ArticleForm

	if request.method == 'POST':
		form = form_class(data=request.POST)
		if form.is_valid():
			art=form.save(commit=False)
			art.author=request.user
			art.save()
		else:
			form = form_class
	return render(request,'Gapp/temps/index.html',{'article':form_class})


# Events Function 
def ActivityData(request):
	form_class = G_forms.EventForm

	if request.method == 'POST':
		form = form_class(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			form = form_class
	return render(request,'Gapp/temps/activities.html',{'form':form_class})
	#modified__year=today.year,modified__month=today.month,modified__day=today.day

# Announcement
# def AnnounceView(request):
# 	if request.method == 'POST':
# 		description = request.POST.get('desc')
# 		G_models.Announcements.objects.create(description=description)
# 		return JsonResponse({'description':description})
# 	else:
# 		return HttpResponse('Request must be POST')

def AnnouncementView(request):
	a = G_models.Announcements.objects.all()
	return render(request,'Gapp/temps/announce.html',{'news':a})
def AnnounceView(request):
    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        response_data = {}

        post = G_models.Announcements(description=post_text,author=request.user)
        post.save()

        response_data['result'] = 'Create post successful!'
        response_data['postpk'] = post.pk
        response_data['text'] = post.description
        response_data['author'] = post.author.username
        

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )