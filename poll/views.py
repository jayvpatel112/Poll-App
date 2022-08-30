from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Poll
from django.db.models import F # from query expression

@login_required(login_url='login')
def home(request):
    if request.method == "POST":
        answer = request.POST.get('answer')
        print(answer)
        information = request.POST.get('info')
        print(information)
        queno_username = list(information.split(" "))

        p = Poll_statistics.objects.filter(username=queno_username[1]) # Filter query by username
        p1 = Poll_statistics.objects.filter(question_no = int(queno_username[0])) # filter query by question no
        p2 = p&p1 # Intersection of two query set

        if answer == 'a':
            p2.update(answer1_count=F('answer1_count')+1)
            p2.update(total_answer=F('total_answer')+1)
        elif answer == 'b':
            p2.update(answer2_count=F('answer2_count')+1)
            p2.update(total_answer=F('total_answer')+1)
        elif answer == 'c':
            p2.update(answer3_count=F('answer3_count')+1)
            p2.update(total_answer=F('total_answer')+1)
        elif answer == 'd':
            p2.update(answer4_count=F('answer4_count')+1)
            p2.update(total_answer=F('total_answer')+1)

    questions = Poll.objects.all()
    return render(request, 'poll/home.html', {'questions': questions})

@login_required(login_url='login')
def poll_statistics_dashboard(request):
    content = Poll_statistics.objects.all()
    return render(request, 'poll/poll_statistics_dashboard.html', {"content" : content})

@login_required(login_url='login')
def create_poll(request):
    form = PollForm(user=request.user)
    context = {'form': form}
    if request.method == "POST":
        form = PollForm(request.POST, user=request.user)
        if form.is_valid():

            count_total_poll_object = Count_total_poll.objects.get(current_user_name=request.user)
            if count_total_poll_object.total_polls <= 5:
                form.save()
                count_total_poll_object.total_polls = count_total_poll_object.total_polls + 1
                count_total_poll_object.save()
                p = Poll_statistics(username=request.user, question_no= count_total_poll_object.total_polls, answer1_count=0, answer2_count=0, answer3_count=0, answer4_count=0, total_answer=0)
                p.save()
            else:
                messages.error(request, "You can create only 5 Questions")
                print("You can create only 5 Questions")

            return redirect('home')
        context = {'form': form}
        return render(request, 'poll/create_poll.html', context)
    return render(request, 'poll/create_poll.html', context)