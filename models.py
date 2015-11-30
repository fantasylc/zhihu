# -*- coding:utf-8 -*-

from django.db import models

# Create your models here.


class string_with_title(str):
    def __new__(cls, value, title):
        instance = str.__new__(cls, value)
        instance._title = title
        return instance

    def title(self):
        return self._title

    __copy__ = lambda self: self
    __deepcopy__ = lambda self, memodict: self

class Answer(models.Model):
    question = models.CharField(max_length=200,verbose_name='问题')
    question_link = models.CharField(max_length='300',verbose_name='问题链接')
    author = models.CharField(max_length=200,default='匿名用户',verbose_name='答题者')
    author_link = models.CharField(max_length=300,verbose_name='作者链接')

    vote = models.IntegerField(verbose_name='赞同数')
    summary = models.TextField(verbose_name='概述')
    summary_img = models.CharField(max_length=500,blank=True,null=True,default=None,verbose_name='概述图')

    answer = models.TextField(verbose_name='答案')
    date = models.DateField(auto_now=True,verbose_name='更新时间')

    class Meta:
        verbose_name = verbose_name_plural = '知乎'
        ordering = ['-date']
        app_label = string_with_title('zhihu', '知乎管理')

    def __str__(self):
        return self.question