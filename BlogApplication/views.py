import datetime

from bs4 import BeautifulSoup
import requests
from .models import Post, About, Category
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, get_object_or_404


@csrf_protect
def post_list(request):
    posts = Post.objects.order_by('-id')

    return render(request, 'BlogApplication/index.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'BlogApplication/post.html', {'post': post})


def about_text(request):
    about = About.objects.get().text
    introduction = About.objects.get().introduction
    image_file = About.objects.get().image
    return render(request, 'BlogApplication/about.html',
                  {'about': about, 'introduction': introduction, 'image_file': image_file})


def search_posts(request):
    if request.method == 'POST':
        search_text = request.POST['search']
    else:
        search_text = ''

    posts = Post.objects.filter(title__contains=search_text)

    return render(request, 'BlogApplication/search_results.html', {'posts': posts})


def category_post_list(request, pk):
    category = get_object_or_404(Category, pk=pk)
    id_of_category = category.id
    posts = ''
    posts = Post.objects.filter(category = id_of_category)

    return render(request, 'BlogApplication/category.html', {'posts': posts})


def regex(request):
    return render(request, 'BlogApplication/regex.html')


def top_20_from_helion(request):
    today = datetime.date.today()
    helion_html = requests.get('http://helion.pl/kategorie/bestsellery')
    soup = BeautifulSoup(helion_html.text, "lxml")
    divTag = soup.find_all("div", {"class": "bestseller-list"})

    books = []
    for tag in divTag:
        liTag = tag.find_all("li")
        for tag in liTag:
            title = ''
            image = ''
            link = ''

            h2Tag = tag.find("h2")
            img = tag.find('img', {'class': 'lazy'})

            if img != None:
                image = img['data-src']

            if h2Tag == None:
                continue
            else:
                for tag in h2Tag:
                    title = tag.text
                    link = tag['href']
            books.append(BookData(title, image, link))

    return render(request, 'BlogApplication/top_20.html', {'books': books, 'date': today})


# pomocnicza klasa Book - do pobierania książek

class BookData:
    title = ''
    image = ''
    link = ''

    def __init__(self, title, image, link):
        self.title = title
        self.image = image
        self.link = link
