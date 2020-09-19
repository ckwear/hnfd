def Posting(request):
    if request.method == "POST":
         posting = MakePost(request.POST)
         if posting.is_valid():
             post = posting.save(commit=False)
             post.author = 'markcha'
             post.published_date = timezone.now()
             post.save()
             return redirect('showtext', pk=post.pk)
    else:
         posting = MakePost()

    return render(request, 'posting.html', {'posting': posting})



def start(request):
    return render(request, 'index.html', {})

def ShowPost(request):
    posts = Post.objects.all()
    return render(request, 'showpost.html', {'posts': posts})

def ShowText(request, pk):
    post = get_object_or_404(Post, pk=pk)
    #Post.objects.get(pk=pk)
    #return HttpResponse(post)
    return render(request, 'showtext.html', {'post' : post})