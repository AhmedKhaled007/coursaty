from django.shortcuts import render , get_object_or_404 , redirect ,reverse

from .models import Post , Comment
from django.contrib import messages



from .forms import PostForm , CommentForm


# Create your views here.

def all_posts(request):
    all_posts = Post.objects.all()
    context = {
        'all_posts' : all_posts ,
    }

    return render(request,'all_posts.html', context)



def post(request , id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.post = post
            new_form.save()
            return redirect(reverse('post'))
    else:
        form = CommentForm()

    context = {
        'form' : form ,
        'post' : post ,
    }

    return render(request,'detail.html', context)



def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('/')


    else :
        form = PostForm()


    
    context = {
        'form' : form ,
    }

    return render(request,'create.html',context)


def edit_post(request , id):
    post = get_object_or_404(Post , id=id)
    if request.method == "POST":
        form = PostForm(request.POST , instance=post )
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('/')


    else :
        form = PostForm(instance=post)


    
    context = {
        'form' : form ,
    }

    return render(request,'edit.html',context)

def comment(request,id):
    if  request.user.is_authenticated:
        mypost=get_object_or_404(Post,id=id)
        myreply=request.POST['text']
        user=request.user
        Comment.objects.create(user=user,post=mypost,reply=myreply)
        return redirect(reverse('post',kwargs={'id':id}))
    else :
        messages.error(request, 'you must  logging first !!!')
        return redirect('login')