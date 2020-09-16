from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Profile, Comment
from .forms import PostForm, ProfileForm, AddCommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        cat_dropdown_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_dropdown_menu'] = cat_dropdown_menu
        return context

class MyProfileView(ListView):
    model = Post
    template_name = 'my_profile.html'
    ordering = ['-id']

def CategoryView(request, cat):
    cat_list = Post.objects.filter(category=cat.replace('-', ' '))
    return render(request, 'category.html', {'cat': cat.title().replace('-', ' '), 'cat_list': cat_list})

class FullArticleView(DetailView):
    model = Post
    template_name = 'full_article.html'

    def get_context_data(self, *args, **kwargs):
        cat_dropdown_menu = Category.objects.all()
        context = super(FullArticleView, self).get_context_data(*args, **kwargs)
        get_total_likes = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = get_total_likes.total_likes()

        liked = False
        if get_total_likes.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['cat_dropdown_menu'] = cat_dropdown_menu
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

class NewArticleView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'new_article.html'

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

class EditArticleView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'edit_article.html'
    success_url = reverse_lazy('my-profile')


class DeleteArticleView(DeleteView):
    model = Post
    template_name = 'delete_article.html'
    success_url = reverse_lazy('home')

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('full-article', args=[str(pk)]))

class EditMyProfileView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'edit_myprofile.html'
    # fields = ['bio', 'profile_pic', 'facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url']
    success_url = reverse_lazy('my-profile')

class CreateMyProfileView(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'create_myprofile.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AddCommentView(CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = 'add_comment.html'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('full-article', kwargs={'pk': self.kwargs['pk']})
