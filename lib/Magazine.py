class Magazine:
    all_magazines = []

    def _init_(self, name, category):
        self.name = name
        self.category = category
        self.articles = []
        Magazine.all_magazines.append(self)

    def article_titles(self):
        return [article.title for article in self.articles]

    def contributors(self):
        authors = [article.author for article in self.articles]
        author_counts = {}
        for author in authors:
            if author in author_counts:
                author_counts[author] += 1
            else:
                author_counts[author] = 1

        return [author for author, count in author_counts.items() if count > 2]

    @classmethod

    def find_by_name(cls, name):
            return next((magazine for magazine in cls.all_magazines if magazine.name == name), None)

    @classmethod
    def all(cls):
            return cls.all_magazines

    def _str_(self):
            return f"{self.name} ({self.category})"





