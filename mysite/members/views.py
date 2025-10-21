from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from members.models import Member
from django.contrib.auth.decorators import login_required
from .forms import MemberForm

# Create your views here.
def register(request):
    '''Adds a new member to the member list

        :return: Returns to main.html or registr.html pages.
        :rtype: html
    '''

    if request.method == 'POST':
        first_name = request.POST.get('first_name', 'TestF')
        last_name = request.POST.get('last_name', 'TestL')
        id_number = request.POST.get('id_number')
        dob = request.POST.get('dob', '1900-01-01')
        email = request.POST.get('email', 'TestE')
        member = Member.objects.create(first_name = first_name, 
                                         last_name = last_name,
                                         id_number = id_number,
                                         dob = dob,
                                         email = email)
        return render(request,"main.html")
    else:
        return render(request,'register.html')
    # form = MemberForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    

def member_list(request):
    '''Generates the list of members to populate the member_list.html.
    
        :param Member latest_member_list: List of Member objects stored
               
        :return: member_list.html
        :rtype: html

    '''
    latest_member_list = Member.objects.order_by('-last_name')[:5]
    context = {'latest_member_list': latest_member_list}
    return render(request, "member_list.html", context)

# def detail(request, id_number):
#     # if request.user.is_authenticated:
#         member = get_object_or_404(Member, pk=id_number)
#         return render(request, 'view_member.html', {'member': member})
#     # else:
#     #     return render(request, 'authentication/login_error.html')