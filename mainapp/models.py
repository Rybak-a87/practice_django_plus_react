from django.db import models



class BlogCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя категории")
    slug = models.SlugField(verbose_name="Слаг категории", unique=True)

    def __str__(self):
        return self.name


class BlogPostQuerySet(models.QuerySet):    # возвращает queryset на выходе <class>.objects.all()
    def find_by_title_in_qs(self, post_title):
        return self.filter(title__icontains=post_title)


class BlogPostManager(models.Manager):    # это атрибут objects из <class>.objects.all()
    def get_queryset(self):
        # return super().get_queryset()
        return BlogPostQuerySet(self.model, using=self._db)

    def all(self):    # это метод all из <class>.objects.all()
        return self.get_queryset().filter(in_archive=False)

    def find_by_title_in_qs(self, post_title):
        return self.get_queryset().find_by_title_in_qs(self, post_title)


class BlogPost(models.Model):
    blog_category = models.ForeignKey(BlogCategory, verbose_name="Имя категории", on_delete=models.CASCADE)    # заключать имя класса в кавычки - когда класс-аргумент ниже этого класса
    title = models.CharField(max_length=255, verbose_name="Название поста")
    slug = models.SlugField(verbose_name="Слаг", unique=True)
    content = models.TextField(verbose_name="Текст")
    image = models.ImageField(upload_to="blog_posts/", blank=True, null=True)
    pub_date = models.DateTimeField(auto_now=True)
    in_archive = models.BooleanField(default=False, verbose_name="В архиве")
    objects = BlogPostManager()    # перезапись атрибута <objects>

    def __str__(self):
        return f"{self.title} из категории '{self.blog_category.name}'"