from .models import News

def news_processor(request):
    news = News.objects.all()
    return {'news_list': news}
