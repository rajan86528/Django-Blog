from django.shortcuts import render, redirect, reverse
from . models import Post
from posts.forms import PostCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})


def post_detail(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post':post,
        'title': post.title
    }
    return render(request, 'posts/detail.html', context)

@login_required
def create_post(request):
    form = PostCreationForm()
    if request.method == "POST":
        form = PostCreationForm(request.POST)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.author = request.user
            form_obj.save()
            return redirect(reverse("homepage"))
    context = {
        "form": form
    }
    return render(request, "posts/createpost.html", context)


@login_required
def delete_post(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('homepage')

    return render(request, 'posts/detail.html', {'post': post})