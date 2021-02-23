from rest_framework import serializers

from ..models import BlogCategory, BlogPost


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = "__all__"


class BlogCategoryDetailSerializer(serializers.ModelSerializer):    # для отрисовки постов в апи категорий
    posts = serializers.SerializerMethodField()    # выводит необходимую информацию

    class Meta:
        model = BlogCategory
        fields = "__all__"

    @staticmethod
    def get_posts(obj):    # для вывода нужной информации (должно быть get_<название поля>)
        return BlogPostSerializer(BlogPost.objects.filter(blog_category=obj), many=True).data


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = "__all__"


class BlogPostListRetrieveSerializer(serializers.ModelSerializer):    # для отрисовки объекта категорий
    blog_category = BlogCategorySerializer()

    class Meta:
        model = BlogPost
        fields = "__all__"
