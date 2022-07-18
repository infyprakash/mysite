from django.shortcuts import render
from polls.models import Question,Choice

# Create your views here.
def home(request):
    data=[]
    questions = Question.objects.all()
    for question in questions:
        choices = Choice.objects.filter(question__id=question.id)
        data.append({question:choices})
    print(data)
    context_dict = {
        'data':data
    }
    return render(request,'index.html',context_dict)

def test(request):
    return render(request,'test.html')

def vote(request,id):
    if(request.method=="POST"):
        data = dict(request.POST)
        print(data)
        id=int(data['question_id'][0])
        form_choice = data['choice'][0]
        question = Question.objects.get(id=id)
        choices = Choice.objects.filter(question__id=id)
        for choice in choices:
            if(choice.choice_text==form_choice):
                choice.votes = choice.votes+1
            choice.save()
        context_dict={
        'question':question,
        'choices':choices
        }
    else:
        question = Question.objects.get(id=id)
        choices = Choice.objects.filter(question__id=id)
        context_dict={
        'question':question,
        'choices':choices
        }
    return render(request,'vote.html',context_dict)


