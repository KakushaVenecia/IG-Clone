from django.shortcuts import redirect, render , get_object_or_404
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate ,login
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http import HttpResponse, Http404,HttpResponseRedirect


ObjectDoesNotExist =404
# Create your views here.
def landing(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "Login Successful")
                return redirect('post')
            else:
                messages.error(request, "Invalid Username or Password")
        else:
            messages.error(request, "Invalid Username or Password")
    form=AuthenticationForm                    
    return render(request, 'landing.html',{"form":form} )

def register(request):
    if request.method=='POST':
        form =newUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successful")
            return redirect('landing')
        messages.error(request, 'Registration Failure')
    form=newUserForm()
    return render(request, 'signup.html',{"register_form":form})

def logout(request):
    messages.success(request, "See you Soon!")
    return redirect('landing')


@login_required(login_url='login')
def profile(request):
    images = Post.objects.all()
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'prof_form': prof_form,
        'images': images,

    }
    return render(request, 'profile.html', context)

@login_required(login_url='login')
def user_profile(request,username):
    profile_user=get_object_or_404(User,username=username)
    if request.user == profile_user:
        return redirect('profile',username=request.user.username)
    user_posts=profile_user.profile.posts.all()

    followers=Follow.objects.filter(followed=profile_user.profile)  
    following=None
    for follower in followers:
        if request.user.profile == follower.follower:
            following=True  
        else:
            following=False
    context = {
        'profile_user':profile_user,
        'user_posts':user_posts,
        'followers':followers,
        'following':following
        }
    return render(request, 'user_profile.html', context)
            
@login_required(login_url='login')
def post(request):
    images = Post.objects.all()
    print(images)
    comments = Comment.objects.all()
    users = User.objects.exclude(id=request.user.id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit = False)
            image.user = request.user.profile
            image.save()
            messages.success(request, f'Successfully uploaded your pic!')
            return redirect('post')
    else:
        form = PostForm()
    return render(request, 'index.html', {"images":images[::-1], "form": form, "users": users, "comments": comments })


def image(request,image_id):
    try:
        image = Post.objects.get(id = image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"image.html", {"image":image})

@login_required 
def comment(request,image_id):
        current_user=request.user
        image = Post.objects.get(id=image_id)
        user_profile = User.objects.get(username=current_user.username)
        comments = Comment.objects.all()
        if request.method == 'POST':
                form = CommentForm(request.POST, request.FILES)
                if form.is_valid():
                        comment = form.save(commit=False)
                        comment.image = image
                        comment.user = request.user
                        comment.save()  
                return redirect('index')
        else:
                form = CommentForm()
        return render(request, 'comment.html',locals())
@login_required
def search_results(request):
    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = Profile.search_profile(search_term)
        message = f"{search_term}"
        return render(request, 'search.html', {"message":message,"profiles": searched_profiles})
    else:
        message = "You haven't searched for any profile"
    return render(request, 'search.html', {'message': message})   
