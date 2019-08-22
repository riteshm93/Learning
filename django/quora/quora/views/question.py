from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import generic

from quora.models import Post
from quora.forms import PostForm


def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('quora:questions'))
    else:
        return render(request, 'quora/index.html')


class QuestionsView(generic.ListView):
    template_name = 'quora/questions.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Post.objects.filter(post_type_id = Post.QUESTION).order_by('-posted_on')


def question(request, post_id):
        question = get_object_or_404(Post, pk = post_id, post_type_id = Post.QUESTION)
        answerform = PostForm()
        answerform.fields['description'].label= ""
        commentform = PostForm()
        commentform.fields['description'].label= ""
        return render(request, 'quora/question.html', {
            'post': question, 
            'answers': question.answers(), 
            'comments': question.comments(),
            'answerform': answerform,
            'commentform': commentform
            })


@login_required(login_url='/quora/')
def new_question(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            form = PostForm()
            form.fields['description'].label= "Question"
            return render(request, 'quora/new-question.html', {'form': form, 'post': Post})
        else:
            return render(request, 'quora/index.html')
