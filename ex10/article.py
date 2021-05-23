#############################################################################################
# FILE : article.py
# WRITER : Bar Aloni
# EXERCISE : intro2cs ex9 2016-2017
# DESCRIPTION : an Article Class. more description in Article documentation
###########################################################################################


class Article:
    """
    A class of items of article. each has in-neighbors- articles it directs to,
    out-neighbors- article that directs to it, rank- by default =1, and a title.
    a representation of article is a tuple, its title and a list of neighbors titles.
    all but its title can change.
    """
    __RANK = 1

    def __init__(self, article_title):
        """
        constructs a new Article object
        :param article_title: String representing an Article title
        """
        self.__title = article_title
        # out-neighbors:
        self.__neighbors = set()
        # in-neighbors:
        self.__entries = set()
        self.__rank = self.__RANK
        # this iteration's addition to rank, in calculating page rank
        self.__iter_rank = 0

    def get_entries(self):
        """
        :return: int representing the amount of the article's in-neighbors
        """
        return len(self.__entries)

    def add_entry(self, other):
        """
        adds an in-neighbor to the article
        :param other: Article object
        """
        self.__entries.add(other)

    def get_rank(self):
        """
        :return: float representing the article's rank
        """
        return self.__rank

    def set_iter_rank(self, rank):
        """
        updates the temporary addition
        :param rank: float representing this iteration's addition to the article's rank
        """
        self.__iter_rank += rank

    def set_rank(self):
        """
        :return: updated the article's rank, taking account this iteration's addition
        """
        self.__rank = self.__iter_rank
        self.__iter_rank = 0

    def get_title(self):
        """
        :return: th article's title
        """
        return self.__title

    def add_neighbor(self, neighbor):
        """
        adds an article object as an out-neighbor of this article
        :param neighbor: article object
        """
        self.__neighbors.add(neighbor)

    def get_neighbors(self):
        """
        :return: a list of the article's out-neighbors
        """
        return list(self.__neighbors)

    def __repr__(self):
        """
        :return: a string representation of the Article, at the form:
         ( 'a', ['b', 'c'])
         where 'a' is this article's title and 'b', 'c' are the title's of 'a' neighbors
        """
        neighbors = [neighbor.get_title() for neighbor in self.__neighbors]
        return "('" + self.__title + "' ," + str(neighbors) + ')'

    def __len__(self):
        """
        :return: int representing the amount of the article's out-neighbors
        """
        return len(self.__neighbors)

    def __contains__(self, article):
        """
        :param article: article object
        :return: true if 'article' is an out-neighbor of this article, false otherwise
        """
        return article in self.__neighbors
