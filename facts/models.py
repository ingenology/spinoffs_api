from random import shuffle

from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=55)


class FactManager(models.Manager):
    def active(self):
        return self.filter(active=True)


class Fact(models.Model):
    NUM_CHOICES = 3

    MAX_LEVELS = 10
    LEVELS = tuple((i, i) for i in xrange(1, 1 + MAX_LEVELS))

    spinoff = models.ForeignKey('archive.Item')
    fact = models.TextField()
    image = models.ImageField(upload_to='facts', blank=True, null=True)
    level = models.IntegerField(choices=LEVELS, default=1)
    categories = models.ManyToManyField(Category, blank=True, null=True)

    question = models.TextField(blank=True)
    answer_text = models.CharField(max_length=255, blank=True)
    answer_image = models.ImageField(upload_to="questions", blank=True, null=True)

    active = models.BooleanField(default=True)

    objects = FactManager()

    def __unicode__(self):
        return u"{}...".format(self.fact[:30])

    def get_choices(self):
        url = self.get_answer_image_url()
        correct = (self.answer_text, url)
        others = (Fact
            .objects
            .exclude(pk=self.pk)
            .filter(level=self.level)
            .order_by('?'))[:self.NUM_CHOICES - 1]

        answers = [(i.answer_text, i.get_answer_image_url()) for i in others] + [correct]
        shuffle(answers)
        return answers

    def get_image_url(self):
        return '' if not self.image else self.image.url

    def get_answer_image_url(self):
        return '' if not self.answer_image else self.answer_image.url
