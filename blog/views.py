from django.shortcuts import render

from blog.models import Category, Post


def home(request):
    name = 'Erick'
    # categories = ['jogos', 'sistemas operacionais', 'desenvolvimento', 'skate']
    # for category in categories:
    #     Category.objects.create(nome=category)
    categories = Category.objects.all()

    # post = Post()
    # post.name = 'Brawlhalla'
    # post.content = 'Brawlhalla é um jogo de luta multplayer online'
    # post.category = categories[0]
    # post.status = 'Published' # 'Draft' 'Published'
    # post.save()

    posts = Post.objects.filter(status='Published')

    context = {
        'name': name,
        'categories': categories,
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)


def show_posts_by_category(request, category_id):
    name = 'Erick'
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    posts = Post.objects.filter(category=category, status='Published')

    context = {
        'name': name,
        'categories': categories,
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)
