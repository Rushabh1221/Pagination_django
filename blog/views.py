from django.shortcuts import render
from .models import Post
#from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from django.http import Http404

#Pagination with Function-Based View:
#def post_list(request):
#    all_post = Post.objects.all().order_by('id')
#    paginator = Paginator(all_post, 3, orphans=1)
#    page_no = request.GET.get('page')
#    page_obj = paginator.get_page(page_no)
#    return render(request, 'blog/home.html', {'page_obj':page_obj})

#Pagination with Class-Based View:
class PostListView(ListView): 
    model = Post
    template_name = 'blog/home.html' 
    ordering = ['id']
    paginate_by = 3
    paginate_orphans = 1

    #def get_context_data(self, *args, **kwargs): -->This is useful when 404 error occurs and when it occur we simply 
    #    try:                                        redirect it to page_no 1..
    #     return super(PostListView, self).get_context_data(*args, **kwargs)
    #    except Http404:
    #        self.kwargs['page'] = 1
    #        return super(PostListView, self).get_context_data(*args, **kwargs)

    def paginate_queryset(self, queryset, page_size):
        try:
         return super(PostListView, self).paginate_queryset(queryset, page_size)
        except Http404:
            self.kwargs['page'] = 1
            return super(PostListView, self).paginate_queryset(queryset, page_size)                

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'
