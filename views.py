from django.shortcuts import render
from .models import Answer
# Create your views here.
def zhindex(request):
    comtext = {}
    answer_list = Answer.objects.all()
    comtext['answer_list'] = answer_list
    return render(request,'zhihu/answerall.html',comtext)


def answer(request,id=None):
    context = {}
    answer = Answer.objects.get(pk=id)
    context['answer'] = answer

    return render(request,'zhihu/answer.html',context)