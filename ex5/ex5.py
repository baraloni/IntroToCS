##############################################################################################
# FILE : ex5.py
# WRITER : Bar Aloni
# EXERCISE : intro2cs ex5 2016-2017
# DESCRIPTION :
# a program that displays to the screen all store products.
# the programs can load different stores (combinations of products), and display them.
# another functionality which the program presents is the user ability to mark some
# products by his choice (create a basket) and save it to his computer, and later on
# load and change it.
# in addition, the program allows the user to compare his basket in several stores
# (by his choice), and get information such as: the basket price, how many items are
# missing and what is the cheapest basket from all of the stores he chose to compare.
##############################################################################################
import xml.etree.ElementTree as ET
from copy import deepcopy

CODE_STYLE = '['
CODE_STYLE_END = ']'
NAME_STYLE = '{'
NAME_STYLE_END = '}'
FINE = 1.25


def get_attribute(store_db, ItemCode, tag):
    """
    :param store_db: a dictionary of dictionaries representing
    a store items where each items has some attributes
    :param ItemCode: int, a key of store_db
    :param tag: one of the item's represented by 'ItemCode' attributes
    :return: the attribute (tag) of an Item with code:
    ItemCode in the given store
    """
    item = store_db[ItemCode]
    tag_val = item[tag]
    return tag_val


def string_item(item):
    """
    :param item: a dictionary where the keys are the product's tags
    :return: Textual representation of an item in a store.
    Returns a string in the format of '[ItemCode] (ItemName)'
    """
    item_code = item['ItemCode']
    item_code_style = CODE_STYLE + item_code + CODE_STYLE_END
    item_name = item['ItemName']
    item_name_style = NAME_STYLE + item_name + NAME_STYLE_END
    return item_code_style + '\t' + item_name_style


def string_store_items(store_db):
    """
    :param store_db: a dictionary of dictionaries representing
    a store items where each items has some attributes
    :return: Textual representation of a store.
    Returns a string in the format of:
    string representation of item1
    string representation of item2
    """
    store_string = ''
    for item_code, item_obj in list(store_db.items()):
        item_str = string_item(item_obj)
        store_string += item_str + '\n'
    return store_string[:-1]  # cuts last '\n'


def read_prices_file(filename):
    """
    Read a file of item prices into a dictionary.  The file is assumed to
    be in the standard XML format of "misrad haclcala".
    :param filename: String,  a path to an XML file
    :return: a tuple: store_id and a store_db,
    where the first variable is the store name
    and the second is a dictionary describing the store. 
    The keys in this db will be ItemCodes of the different items and the
    values smaller  dictionaries mapping attribute names to their values.
    Important attributes include 'ItemCode', 'ItemName', and 'ItemPrice'
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    store_id_element = root.find('StoreId')
    store_id = store_id_element.text
    store_db = create_store_db(root)
    return store_id, store_db


def create_store_db(root):
    """
    :param root: a root of a store object
    :return: a dict of dicts where the keys are the store's item's codes,
    and the values are dictionaries which keys are the item's attributes.
    """
    store_db = {}
    item_dict = {}
    items_element = root.find('Items')
    for item in items_element.findall('Item'):
        item_code = ''
        for tag in item:
            item_key = tag.tag
            item_val = tag.text
            item_dict[item_key] = item_val
            if item_key == 'ItemCode':
                item_code = item_val
        store_db[item_code] = item_dict
        item_dict = {}
    return store_db


def filter_store(store_db, filter_txt):  
    """
    :param store_db: a dictionary of dictionaries as created in read_prices_file.
    :param filter_txt: the filter text as given by the user.
    :return: a new dictionary that includes only the items
    that were filtered by user.
    I.e. items that text given by the user is part of their ItemName.
    """
    filtered_dict = {}
    items_codes = store_db.keys()
    for item_code in items_codes:
        item_dict = store_db[item_code]
        item_name = item_dict['ItemName']
        if filter_txt in item_name:
            filtered_dict[item_code] = item_dict
    return filtered_dict


def create_basket_from_txt(basket_txt): 
    """
    :param basket_txt: text representation of few items (and maybe some garbage
      at the edges)
    :return: a basket- list of ItemCodes that were included in basket_txt
    """
    codes_basket = []
    start_idx = basket_txt.find(CODE_STYLE)
    for end_idx in range(start_idx+1, len(basket_txt)):
        if (basket_txt[end_idx] is CODE_STYLE_END) & (start_idx is not None):
            codes_basket.append(basket_txt[start_idx + 1: end_idx])
            start_idx = None
        elif basket_txt[end_idx] is CODE_STYLE:
            start_idx = end_idx
    return codes_basket


def get_basket_prices(store_db, basket):
    """
    :param store_db: dictionary of dictionaries
    :param basket: a list of ItemCodes
    :return: a list of floats (prices). In case one of the items
    is not part of the store, its price will be None.
    """
    prices = [None] * len(basket)
    for basket_idx in range(len(basket)):
        item_code = basket[basket_idx]
        if item_code in store_db.keys():
            item_info = store_db[item_code]
            item_price = item_info['ItemPrice']
            prices[basket_idx] = float(item_price)
    return prices


def sum_basket(price_list):
    """
    :param price_list: a list of prices
    :return: a tuple - the sum of the list (when ignoring Nones)
    and the number of missing items (Number of Nones)
    """
    sum_price_list, missing_items = 0, 0
    for price in price_list:
        if price is not None:
            sum_price_list += price
        else:
            missing_items += 1
    return sum_price_list, missing_items


def basket_item_name(stores_db_list, ItemCode): 
    """
    :param stores_db_list: a list of stores (list of dictionaries of
    dictionaries)
    :param ItemCode: a string of ints
    :return: Find the first store in the list that contains the item and
    return its string representation (as in string_item())
    If the item is not available in any of the stores return only [ItemCode]
    """
    item_name = None
    for store in stores_db_list:
        if ItemCode in store.keys():
            item = store[ItemCode]
            item_name = string_item(item)
    if item_name is None:
        return CODE_STYLE + ItemCode + CODE_STYLE_END
    return item_name


def save_basket(basket, filename):
    """
    :param basket: a list of ItemCodes
    :param filename: a string representing the name of file
    :return: Save the basket into a file. The basket
    representation in the file will be in the following format:
    [ItemCode1] 
    [ItemCode2] 
    ...
    [ItemCodeN]
    """
    file = open(filename, 'w')
    styled_basket = []
    for item_code in basket:
        item_code = CODE_STYLE + item_code + CODE_STYLE_END
        styled_basket.append(item_code)
    file.write('\n'.join(styled_basket))
    file.close()


def load_basket(filename):
    """
    :param filename: a String representing a file name.
    The file is assumed to be in the format of:
    [ItemCode1]
    [ItemCode2]
    ...
    [ItemCodeN]
    :return:
    Create basket (list of ItemCodes) from the given file.
    """
    file = open(filename, 'r')
    lines = file.readlines()
    basket = []
    for item_code in lines:
        item_code = item_code.replace(CODE_STYLE, '')
        item_code = item_code.replace(CODE_STYLE_END, '')
        item_code = item_code.replace('\n', '')
        basket.append(item_code)
    return basket


def best_basket(list_of_price_list):
    """
    :param list_of_price_list: list of lists, where each inner list is
    list of prices as created by get_basket_prices.
    :return: the cheapest store (index of the cheapest list) given that a
    missing item has a price of its maximal price in the other stores *1.25
    """
    list_of_lists = deepcopy(list_of_price_list)
    for inner_idx in range(len(list_of_price_list[0])):  # index of the prices
        prices_lst = []
        for outer_idx in range(len(list_of_price_list)):  # index of the lists of prices
            item = list_of_price_list[outer_idx][inner_idx]
            if item is None:
                item = 0
            prices_lst.append(item)
        fine = FINE * max(prices_lst)
        for price_idx in range(len(prices_lst)):  # index of prices for the same item
            if prices_lst[price_idx] is 0:
                list_of_lists[price_idx][inner_idx] = fine
    for lst_idx in range(len(list_of_price_list)):  # index of the lists of prices
        list_of_lists[lst_idx] = sum(list_of_lists[lst_idx])
    cheapest = min(list_of_lists)
    return list_of_lists.index(cheapest)


