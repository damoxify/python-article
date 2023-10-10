import Magazine

class Article:
    def _init_(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        self.author.articles.append(self)
        self.magazine.articles.append(self)

    def author(self):
        return self.author

    def magazine(self):
        return self.magazine

    @classmethod
    def all(cls):
        return [article for magazine in Magazine.all_magazines for article in magazine.articles]

    def _str_(self):
        return f"{self.title} by {self.author} in {self.magazine}"