import Article
class Author:
    def _init_(self, name):
        self.name = name
        self.articles = []

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self.articles.append(article)

    def articles(self):
        return self.articles

    def magazines(self):
        return list(set([article.magazine for article in self.articles]))

    def topic_areas(self):
        return list(set([magazine.category for magazine in self.magazines()]))

    def _str_(self):
        return self.name
