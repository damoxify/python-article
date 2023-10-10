import unittest
from Author import Author
from Magazine import Magazine
from Article import Article

class TestMagazineAuthorArticle(unittest.TestCase):

    def setUp(self):
        self.author1 = Author("John Doe")
        self.author2 = Author("Jane Smith")
        self.magazine1 = Magazine("Tech Review", "Technology")
        self.magazine2 = Magazine("Fashion Weekly", "Fashion")
        self.article1 = Article(self.author1, self.magazine1, "The Future of AI")
        self.article2 = Article(self.author2, self.magazine2, "Spring Fashion Trends")

    def test_author_name(self):
        self.assertEqual(self.author1.name, "John Doe")
        self.assertEqual(self.author2.name, "Jane Smith")

    def test_magazine_name_category(self):
        self.assertEqual(self.magazine1.name, "Tech Review")
        self.assertEqual(self.magazine1.category, "Technology")
        self.assertEqual(self.magazine2.name, "Fashion Weekly")
        self.assertEqual(self.magazine2.category, "Fashion")

    def test_article_title(self):
        self.assertEqual(self.article1.title, "The Future of AI")
        self.assertEqual(self.article2.title, "Spring Fashion Trends")

    def test_author_articles(self):
        self.assertIn(self.article1, self.author1.articles())
        self.assertIn(self.article2, self.author2.articles())

    def test_author_magazines(self):
        self.assertIn(self.magazine1, self.author1.magazines())
        self.assertIn(self.magazine2, self.author2.magazines())

    def test_article_author(self):
        self.assertEqual(self.article1.author, self.author1)
        self.assertEqual(self.article2.author, self.author2)

    def test_article_magazine(self):
        self.assertEqual(self.article1.magazine, self.magazine1)
        self.assertEqual(self.article2.magazine, self.magazine2)

    def test_magazine_contributors(self):
        self.assertEqual(self.magazine1.contributors(), ["John Doe"])
        self.assertEqual(self.magazine2.contributors(), ["Jane Smith"])

    def tearDown(self):
        del self.author1
        del self.author2
        del self.magazine1
        del self.magazine2
        del self.article1
        del self.article2

if _name_ == '_main_':
   unittest.main()