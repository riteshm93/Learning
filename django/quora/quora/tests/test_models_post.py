import pytest

from quora.models import Post
from django.contrib.auth.models import User

@pytest.fixture
def user(request):
    return User(id=1, username='user1')


@pytest.mark.django_db
def test_question_can_be_posted(user):
    question = Post(id=1, post_type_id=Post.QUESTION, description="Test Question", posted_by=user)
    question.save()
    post = Post.objects.get(pk=1)
    assert question.description == post.description


@pytest.mark.django_db
def test_answer_can_be_posted_to_question(user):
    question = Post(id=1, post_type_id=Post.QUESTION, description="Test Question", posted_by=user)
    answer = Post(id=2, post_type_id=Post.ANSWER, description="Test Answer", parent_id=1, posted_by=user)
    answer.save()
    post = Post.objects.get(pk=2)
    assert answer.description == post.description


@pytest.mark.django_db
def test_comment_can_be_posted_to_question(user):
    question = Post(id=1, post_type_id=Post.QUESTION, description="Test Question", posted_by=user)
    comment = Post(id=2, post_type_id=Post.COMMENT, description="Test Comment", parent_id=1, posted_by=user)
    comment.save()
    post = Post.objects.get(pk=2)
    assert comment.description == post.description


@pytest.mark.django_db
def test_comment_can_be_posted_to_answer(user):
    question = Post(id=1, post_type_id=Post.QUESTION, description="Test Question", posted_by=user)
    answer = Post(id=2, post_type_id=Post.ANSWER, description="Test Answer", parent_id=1, posted_by=user)
    comment = Post(id=3, post_type_id=Post.COMMENT, description="Test Comment", parent_id=2, posted_by=user)
    comment.save()
    post = Post.objects.get(pk=3)
    assert comment.description == post.description


def test_get_root_parent_id_for_question():
    question = Post(id=1, post_type_id=Post.QUESTION)
    assert 1 == question.get_root_parent_id()


def test_get_root_parent_id_for_answer():
    question = Post(id=1, post_type_id=Post.QUESTION)
    answer = Post(id=2, post_type_id=Post.ANSWER, parent = question)
    assert 1 == answer.get_root_parent_id()


def test_get_root_parent_id_for_question_comment():
    question = Post(id=1, post_type_id=Post.QUESTION)
    comment = Post(id=2, post_type_id=Post.COMMENT, parent = question)
    assert 1 == comment.get_root_parent_id()


def test_get_root_parent_id_for_answer_comment():
    question = Post(id=1, post_type_id=Post.QUESTION)
    answer = Post(id=2, post_type_id=Post.ANSWER, parent = question)
    comment = Post(id=3, post_type_id=Post.COMMENT, parent = answer)
    assert 1 == comment.get_root_parent_id()


@pytest.mark.django_db
def test_question_can_not_have_parent_id(user):
    with pytest.raises(Exception) as e:
        question = Post(id=1, post_type_id=Post.QUESTION, posted_by=user, parent_id=1)
        question.save()
    assert 'Question should have null parent id' in str(e.value)


@pytest.mark.django_db
def test_answer_must_have_parent_id(user):
    with pytest.raises(Exception) as e:
        answer = Post(id=1, post_type_id=Post.ANSWER, posted_by=user)
        answer.save()
    assert 'Parent id cant be null for answers and comments' in str(e.value)


@pytest.mark.django_db
def test_comment_must_have_parent_id(user):
    with pytest.raises(Exception) as e:
        comment = Post(id=1, post_type_id=Post.COMMENT, posted_by=user)
        comment.save()
    assert 'Parent id cant be null for answers and comments' in str(e.value)


@pytest.mark.django_db
def test_answer_can_not_be_posted_to_answer(user):
    with pytest.raises(Exception) as e:
        question = Post(id=1, post_type_id=Post.QUESTION, description="Test Question", posted_by=user)
        valid_answer = Post(id=2, post_type_id=Post.ANSWER, description="Test Valid Answer", parent_id=1, posted_by=user)
        invalid_answer = Post(id=3, post_type_id=Post.ANSWER, description="Test Invalid Answer", parent_id=2, posted_by=user)
        invalid_answer.save()
    assert 'Invalid parrent id' in str(e.value)


@pytest.mark.django_db
def test_answer_can_not_be_posted_to_comments(user):
    with pytest.raises(Exception) as e:
        question = Post(id=1, post_type_id=Post.QUESTION, description="Test Question", posted_by=user)
        valid_answer = Post(id=2, post_type_id=Post.ANSWER, description="Test Valid Answer", parent_id=1, posted_by=user)
        comment = Post(id=3, post_type_id=Post.COMMENT, description="Test Comment", parent_id=2, posted_by=user)
        invalid_answer = Post(id=4, post_type_id=Post.ANSWER, description="Test Invalid Answer", parent_id=3, posted_by=user)
        invalid_answer.save()
    assert 'Invalid parrent id' in str(e.value)


@pytest.mark.django_db
def test_comments_can_not_be_posted_to_comments(user):
    with pytest.raises(Exception) as e:
        question = Post(id=1, post_type_id=Post.QUESTION, description="Test Question", posted_by=user)
        answer = Post(id=2, post_type_id=Post.ANSWER, description="Test Answer", parent_id=1, posted_by=user)
        valid_comment = Post(id=3, post_type_id=Post.COMMENT, description="Test Valid Comment", parent_id=2, posted_by=user)
        invalid_comment = Post(id=4, post_type_id=Post.COMMENT, description="Test Invalid Comment", parent_id=3, posted_by=user)
        invalid_comment.save()
    assert 'Invalid parrent id' in str(e.value)


@pytest.mark.django_db
def test_upvotes_count_can_not_be_negative(user):
    with pytest.raises(Exception) as e:
        question = Post(id=1, post_type_id=Post.QUESTION, description="Test Question", up_votes=-1, posted_by=user)
        question.save()
    assert 'Invalid up_votes, Upvote should be a non-negative integer' in str(e.value)


@pytest.mark.django_db
def test_downvotes_can_not_be_negative(user):
    with pytest.raises(Exception) as e:
        question = Post(id=1, post_type_id=Post.QUESTION, description="Test Question", down_votes=-1, posted_by=user)
        question.save()
    assert 'Invalid udown_votes, Downvote should be a non-negative integer' in str(e.value)


'''
@pytest.mark.django_db
def test_get_answers_for_questions(user):
    question = Post(id=1, post_type_id=Post.QUESTION)
    answer = Post(id=2, post_type_id=Post.ANSWER, parent = question)
    comment = Post(id=3, post_type_id=Post.COMMENT, parent = answer)
'''
