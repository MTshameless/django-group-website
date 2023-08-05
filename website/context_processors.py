from .models import category


def get_category(request):
    return {
        'categories': category.objects.all()
    }