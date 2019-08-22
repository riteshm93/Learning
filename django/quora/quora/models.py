import datetime

from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User


class Post(models.Model):
    QUESTION = 1
    ANSWER = 2
    COMMENT = 3
    post_type_id = models.IntegerField(null=False)
    description = models.TextField()
    posted_on = models.DateTimeField('date posted', auto_now_add=True)
    last_updated = models.DateTimeField('date updated', auto_now_add=True)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    parent = models.ForeignKey('Post', on_delete=models.CASCADE, null=True)
    posted_by = models.ForeignKey(User)

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        if self.post_type_id == self.QUESTION and self.parent_id is not None:
            raise Exception('Question should have null parent id')
        elif int(self.post_type_id) != self.QUESTION and self.parent_id is None:
            raise Exception('Parent id cant be null for answers and comments')
        elif self.post_type_id == self.ANSWER and self.parent_id != self.QUESTION:
            raise Exception('Invalid parrent id')
        elif self.post_type_id == self.COMMENT and self.parent_id == self.COMMENT:
            raise Exception('Invalid parrent id')
        elif self.up_votes < 0:
            raise Exception('Invalid up_votes, Upvote should be a non-negative integer')
        elif self.down_votes < 0:
            raise Exception('Invalid udown_votes, Downvote should be a non-negative integer')
        else:
            super(Post, self).save(*args, **kwargs)

    def get_root_parent_id(self):
        '''
        - get root parent id (question id) for the post
        Returns: int
        '''
        if self.parent_id is None:
            return self.id
        else:
            return self.parent.get_root_parent_id()

    def answers(self):
        '''
        - get all the answers for the post
        '''
        return self.post_set.filter(post_type_id = self.ANSWER).order_by('-last_updated')

    def comments(self):
        '''
        - get all the comments for the post
        '''
        return self.post_set.filter(post_type_id = self.COMMENT).order_by('-last_updated')


class Vote(models.Model):
    UPVOTE = 'U'
    DOWNVOTE = 'D'
    NONE = 'N'

    CHOICES = (
        (UPVOTE, 'Upvote'),
        (DOWNVOTE, 'Downvote'),
        (NONE, 'None')
    )
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=CHOICES, default=NONE)
    user = models.ForeignKey(User)
    unique_together = ('post', 'user')

    def __str__(self):
        return self.type

    def save(self, *args, **kwargs):
        if self.post.posted_by_id == self.user_id:
            raise Exception('User cant vote on their own posts')
        else:
            super(Vote, self).save(*args, **kwargs)

    def vote(self, choice):
        '''
        - updates the user choice (upvote or downvote or None)
        Args:
            choice (string) - upvote/downvote from VOTE_CHOICES
        Returns: None
        '''
        if self.type == choice:
            '''Set type to none if same type is selected again'''
            self.type = self.NONE
        else:
            self.type = choice
        self.save()


@receiver(models.signals.post_save, sender=Vote)
def update_votes_count(sender, instance, **kwargs):
    '''
    - updates total upvotes/downvotes count for the post
    '''
    post = instance.post
    post.up_votes = post.vote_set.filter(type=Vote.UPVOTE).count()
    post.down_votes = post.vote_set.filter(type=Vote.DOWNVOTE).count()
    post.save()
