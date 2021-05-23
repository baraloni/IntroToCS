#############################################################################################
# FILE : wikinetwork.py
# WRITER : Bar Aloni
# EXERCISE : intro2cs ex9 2016-2017
# DESCRIPTION : an WikiNetwork Class. and a static method:
# read_article_links(file_name): create a list form the file's data
# more description in WikiNetwork documentation
###########################################################################################
from article import Article


def read_article_links(file_name):
    """
    create a list form the file's data
    :param file_name: String representing a name of a file of the form:
    x\ty
    ...
    u\tv
    :return: a list of string tuples (x, y), where x, y represents an article title,
    and y is a direct successor of x.
    """
    links_list = []
    for line in open(file_name):
        couple = line.split('\t')
        couple[1] = couple[1].replace('\n', '')
        links_list.append(tuple(couple))
    return links_list


class WikiNetwork:
    """
    a class of WikiNetwork - receives a list of tuples, and creates
    Article instances, and connects them. connections - updates it's articles
    in-neighbors, out-neighbors, rank them by page-rank algorithm or jaccard algorithm,
    find paths between them and 'walk' by them, or get all neighbors of depth lower or
    equal to a certain depth.
    """

    def __init__(self, link_list):
        """
        constructs a new WikiNetwork object
        :param link_list: a list of string tuples (x, y), where x, y represents an article title,
        and y is a direct successor of x.
        """
        self.__link_list = link_list
        # all articles objects on net , ordered by their titles:
        self.__articles = self.__update_given_network({}, self.__link_list)

    def __update_given_network(self, dict, link_list):
        """
        given a "network" at the form of a dictionary and a list of article titles tuples,
        add the article objects corresponding to the titles of the tuples to the dict under their title.
        every object holds it's neighbors list: the list of the direct successors, according to "link_list"
        :param dict: a dictionary, which it's keys are article titles
        and it's values are the article objects matching the title
        :param link_list: a list of tuples (x, y) when x, y are article titles (strings)
         and y is a directed successor of x.
        :return: the updated dict, where each of it's values neighbors list is also updated
        """
        for title_1, title_2 in link_list:
            if title_1 not in dict.keys():
                article_1 = Article(title_1)
                dict[title_1] = article_1
            else:
                article_1 = dict[title_1]
            if title_2 not in dict.keys():
                article_2 = Article(title_2)
                dict[title_2] = article_2
            else:
                article_2 = dict[title_2]
            article_1.add_neighbor(article_2)
            article_2.add_entry(article_1)
        return dict

    def __contains__(self, title):
        """
        :param title: String representing an Article title
        :return: true if the Article named "title" is in the network, False otherwise
        """
        return title in self.__articles.keys()

    def __len__(self):
        """
        :return: int, the number of articles in the network
        """
        return len(self.__articles.keys())

    def __repr__(self):
        """
        :return: a string representation of the network, at the form of:
        {‘a’: (‘a’, [‘b’, ’c’]), ‘b’: (‘b’, []), ‘c’: (‘c’, [])}
        when 'a', 'b', 'c' are network's articles titles, and 'b','c' are
        direct successor of 'a' and 'b', 'c' have no successors
        """
        return str(self.__articles)

    def __getitem__(self, title):
        """
        :param title: String representing an Article title
        :return: the Article object named "title" , if it is a part of the network,
        raises a KeyError otherwise
        """
        if title in self.__articles.keys():
            return self.__articles[title]
        raise KeyError(title)

    def get_articles(self):
        """
        :return: a list of all Article objects in the network
        """
        return [article_obj for article_obj in self.__articles.values()]

    def get_titles(self):
        """
        :return: a list of Strings representing all Articles titles in Network
        """
        return [title for title in self.__articles.keys()]

    def __update_network(self, link_list):
        """
        updates the network to contain all article objects matching the titles given
        in "link_list", where each object's neighbors list is also updated according
        to "link_list"
        :param link_list: a list of string tuples (x, y), where x, y represents an
        article title, and y is a direct successor of x.
        """
        self.__articles = self.__update_given_network(self.__articles, link_list)

    def page_rank(self, iters, d=0.9):
        """
        :param iters: int representing the number of rounds
        :param d: a float between 0 to 1
        :return: a list of the net's articles titles ordered in a descending order of
        it's rank. in case of several articles with same rank: they will be presented
        in an alphabetically order.
        """
        for iter in range(iters):
            for article in self.__articles.values():
                if len(article) is not 0:
                    distribute = d * article.get_rank() / len(article)
                    for neighbor in article.get_neighbors():
                        neighbor.set_iter_rank(distribute)
                article.set_iter_rank(1-d)
            for article in self.__articles.values():
                article.set_rank()
        return self.__sort_by_value([(article.get_title(), article.get_rank()) for article in self.get_articles()])

    def __sort_by_value(self, lst):
        """
        :param lst: a list of tuples (x,y) where x is a string representing the article's title
        and y is an int representing it's valu
        :return: the lst sorted by descending y values, and alphabetically order
        """
        sorted_articles = sorted(lst, key=lambda item: (-item[1], item[0]))
        return [article_title for (article_title, article_rank) in sorted_articles]

    def jaccard_index(self, article_title):
        """
        :param article_title: string representing an Article title
        :return: a list of the net's Article's titles, ordered by their
        neighbors_intersection/neighbors_union value with the article whose title was given.
        the articles are sorted in a descending order. if several article produce the same
        ration, they will be ordered alphabetically.
        """
        lst = []
        if self.__contains__(article_title):
            article = self.__getitem__(article_title)
            if article.get_neighbors != []:
                for other in self.get_articles():
                    union = set(article.get_neighbors()).union(set(other.get_neighbors()))
                    if len(union) != 0:
                        intersection = set(article.get_neighbors()).intersection(set(other.get_neighbors()))
                        ratio = len(intersection) / len(union)
                        lst.append((other.get_title(), ratio))
                return self.__sort_by_value(lst)
        return None

    def travel_path_iterator(self, article_title):
        """
        returns a generator
        :param article_title: string representing an Article title
        :return: if article does not exist in thr Net- returns an empty iterator
        otherwise: return an iterator which works as follows:
        first it will return the title of the article.
        in the next iter it will return the title of the article's neighbor whose
        entries val is the greatest. in case of several neighbor with the same
        entries val: the one to be returned is decided alphabetically.
        """
        if article_title in self.__articles:
            article = self.__getitem__(article_title)
            yield article.get_title()
            while article.get_neighbors() != []:
                lst = [(neighbor.get_title(), neighbor.get_entries()) for neighbor in article.get_neighbors()]
                sorted_lst = self.__sort_by_value(lst)
                yield sorted_lst[0]
                article = self.__getitem__(sorted_lst[0])
            raise StopIteration
        else:
            raise StopIteration

    def friends_by_depth(self, article_title, depth):
        """
        :param article_title: string representing an Article title
        :param depth: un negative int
        :return: None if article_title is not in the Net.
        otherwise: a list of all neighbors titles in depth <='depth' from the
        article named 'article_title'
        """
        neighbors = set()
        if article_title in self.__articles:
            article = self.__getitem__(article_title)
            neighbors.add(article)
            for iteration in range(depth):
                neighbors = self.neighbors_of_neighbors(neighbors)
            return [neighbor.get_title() for neighbor in neighbors]
        return None

    def neighbors_of_neighbors(self, neighbors):
        """
        :param neighbors: set of articles objects
        :return: a new set containing the original neighbors given in 'neighbors'
        and their neighbors
        """
        new_neighbors = set()
        for article in neighbors:
            for neighbor in article.get_neighbors():
                new_neighbors.add(neighbor)
        return new_neighbors.union(neighbors)
