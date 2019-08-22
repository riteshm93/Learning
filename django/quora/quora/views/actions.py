from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils import timezone

from quora.models import Post, Vote
from quora.forms import PostForm


@login_required(login_url='/quora/')
def new_post(request, post_type_id, post_id=None):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post()
            post.post_type_id = post_type_id
            post.description = request.POST['description']
            if post_type_id != Post.QUESTION:
                post.parent_id = post_id
            post.posted_by = request.user
            post.save()
            return HttpResponseRedirect(get_redirect_url(post))
        else:
            return HttpResponse("Invalid Input.")


@login_required(login_url='/quora/')
def details(request, post_id):
    if request.method == 'GET':
        post = get_object_or_404(Post, pk = post_id)
        return render(request, 'quora/post.html', {'post': post})


@login_required(login_url='/quora/')
def edit(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    if post.posted_by_id != request.user.id:
        return HttpResponse("Not authorized.")

    if request.method == 'GET':
        form = PostForm({'description': post.description})
        form.fields['description'].label = ""
        return render(request, 'quora/edit-post.html', {
            'form': form,
            'post_id': post_id})
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post.description = request.POST['description']
            post.last_updated = timezone.now()
            post.save()
            return HttpResponseRedirect(get_redirect_url(post))
        else:
            return HttpResponse("Invalid Input.")


@login_required(login_url='/quora/')
def delete(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk = post_id)
        if post.posted_by == request.user:
            question_id = post.get_root_parent_id()
            post.delete()
            if question_id == int(post_id):
                return HttpResponseRedirect(reverse('quora:index'))
            else:
                return HttpResponseRedirect(reverse('quora:question_detail', args=[question_id]))
        return HttpResponse("Not authorized.")


@login_required(login_url='/quora/')
def vote(request, post_id):
    if request.method == 'POST':
        try:
            post_vote = Vote.objects.get(post_id=post_id, user_id=request.user.id)
            post_vote.vote(request.POST['choice'])
        except Vote.DoesNotExist:
            post_vote = Vote.objects.create(post_id=post_id, user_id=request.user.id, type=request.POST['choice'])
        return HttpResponseRedirect(get_redirect_url(post_vote.post))

def get_redirect_url(post):
    root_post_id = post.get_root_parent_id()
    return reverse('quora:question_detail', args=[root_post_id])
