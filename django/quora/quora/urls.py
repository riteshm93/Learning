from django.conf.urls import url
from quora.views import user, question, actions

app_name='quora'
urlpatterns = [
    url(r'^$', question.index, name='index'),
    url(r'^login/$', user.login, name='login'),
    url(r'^signup/$', user.signup, name='signup'),
    url(r'^logout/$', user.logout, name='logout'),
    url(r'^questions/$', question.QuestionsView.as_view(), name='questions'),
    url(r'^question/(?P<post_id>[0-9]+)/$', question.question, name='question_detail'),
    url(r'^new_question/$', question.new_question, name='new_question'),
    url(r'^new_post/(?P<post_type_id>[0-9]+)/$', actions.new_post, name='post_question'),
    url(r'^new_post/(?P<post_type_id>[0-9]+)/(?P<post_id>[0-9]+)/$', actions.new_post, name='new_post'),
    url(r'^details/(?P<post_id>[0-9]+)/$', actions.details, name='details'),
    url(r'^edit/(?P<post_id>[0-9]+)/$', actions.edit, name='edit'),
    url(r'^delete/(?P<post_id>[0-9]+)/$', actions.delete, name='delete'),
    url(r'^vote/(?P<post_id>[0-9]+)/$', actions.vote, name='vote'),
]
