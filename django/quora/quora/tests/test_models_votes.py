import pytest

from quora.models import Post, Vote
from django.contrib.auth.models import User

@pytest.fixture
def post(request):
    user = User(id=1, username='user1')
    post = Post(post_type_id=Post.QUESTION, posted_by=user)
    post.save()
    return post

@pytest.fixture
def vote(request, post):
    user = User(id=2, username='user2')
    return Vote(post=post, user=user)


type = (("type"), 
           [
               ("NONE"), ("UPVOTE"), ("DOWNVOTE"),
           ])

choices = (("old_choice", "new_choice", "result_choice"), 
           [
               ("NONE", "UPVOTE", "UPVOTE"),
               ("NONE", "DOWNVOTE", "DOWNVOTE"),
               ("NONE", "NONE", "NONE"),
               ("UPVOTE", "DOWNVOTE", "DOWNVOTE"),
               ("UPVOTE", "UPVOTE", "NONE"),
               ("UPVOTE", "NONE", "NONE"),
               ("DOWNVOTE", "UPVOTE", "UPVOTE"),
               ("DOWNVOTE", "DOWNVOTE", "NONE"),
               ("DOWNVOTE", "NONE", "NONE"),
           ])

votes_count = (("old_choice", "new_choice", "old_upvote_count", "new_upvote_count", "old_downvote_count", "new_downvote_count"), 
           [
               ("NONE", "UPVOTE", 0, 1, 0, 0),
               ("NONE", "DOWNVOTE", 0, 0, 0, 1),
               ("UPVOTE", "DOWNVOTE", 1, 0, 0, 1),
               ("UPVOTE", "UPVOTE", 1, 0, 0, 0),
               ("DOWNVOTE", "UPVOTE", 0, 1, 1, 0),
               ("DOWNVOTE", "DOWNVOTE", 0, 0, 1, 0),
           ])

@pytest.mark.parametrize(*choices)
@pytest.mark.django_db
def test_final_vote_output_after_voting(old_choice, new_choice, result_choice, post, vote):
    vote.type = old_choice[0]
    vote.save()
    vote.vote(new_choice[0])
    assert result_choice[0] == vote.type


@pytest.mark.parametrize(*type)
@pytest.mark.django_db
def test_user_cant_vote_on_their_posts(type, post):
    with pytest.raises(Exception) as e:
        user = User(id=1, username='user1')
        vote = Vote(post=post, user=user)
        vote.type = type[0]
        vote.save()
    assert 'User cant vote on their own posts' in str(e.value)


@pytest.mark.parametrize(*votes_count)
@pytest.mark.django_db
def test_total_votes_count_after_voting(old_choice, new_choice, old_upvote_count, new_upvote_count, old_downvote_count, new_downvote_count, post, vote):
    vote.type = old_choice[0]
    vote.save()
    assert old_upvote_count == vote.post.up_votes
    assert old_downvote_count == vote.post.down_votes
    vote.vote(new_choice[0])
    assert new_upvote_count == vote.post.up_votes
    assert new_downvote_count == vote.post.down_votes

