from django.test import TestCase
from articles.models import Article
from django.utils.text import slugify

# Create your tests here.

class ArticleTestCase(TestCase):

    def setUp(self) -> None:
        self.number_of_objects = 5
        for i in range(0, self.number_of_objects):
            Article.objects.create(title="hello world", 
                               content = "Something else")

    def test_querset_exists(self):
        qs = Article.objects.all()
        self.assertTrue(qs.exists())

    def test_queryset_count(self):
        qs = Article.objects.all()
        self.assertEqual(qs.count(), self.number_of_objects)

    # def test_the_dummy_unique_slug(self):
    #     qs = Article.objects.exclude(slug__iexact='the-dummy')
    #     for obj in qs:
    #         title = obj.title
    #         slug = obj.slug
    #         slugfield_title = slugify(title)
    #         self.assertNotEqual(slug, slugfield_title)
    
    def test_article_search_manager(self):
        qs = Article.objects.search(query="hello world")
        self.assertEqual(qs.count(), self.number_of_objects)
    
