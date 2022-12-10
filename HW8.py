import matplotlib.pyplot as plt
import os
import sqlite3
import unittest

def get_restaurant_data(db_filename):
    """
    This function accepts the file name of a database as a parameter and returns a list of
    dictionaries. The key:value pairs should be the name, category, building, and rating
    of each restaurant in the database.
    """
    con = sqlite3.connect(db_filename)

    cur = con.cursor()
    rest_dict={}
    lister=[]

    # The result of a "cursor.execute" can be iterated over by row
    for row in cur.execute('SELECT restaurants.id,restaurants.name,restaurants.rating,categories.category,buildings.building FROM restaurants JOIN buildings on buildings.id=restaurants.building_id JOIN categories on categories.id=restaurants.category_id'):
        rest_dict={}
        rest_dict["name"]=row[1]
        rest_dict["category"]=row[3]
        rest_dict["building"]=row[4]
        rest_dict["rating"]=row[2]
        lister.append(rest_dict)
    return lister
    con.close()
    pass
def barchart_restaurant_categories(db_filename):
    """
    This function accepts a file name of a database as a parameter and returns a dictionary. The keys should be the
    restaurant categories and the values should be the number of restaurants in each category. The function should
    also create a bar chart with restaurant categories and the counts of each category.
    """
    con = sqlite3.connect(db_filename)

    cur = con.cursor()
    cat_dict={}
    for row in cur.execute('SELECT restaurants.id,restaurants.name,categories.category,categories.id FROM restaurants JOIN categories on categories.id=restaurants.category_id'):
        count=0
        if row[2] not in cat_dict:
            cat_dict[row[2]]=0
        if row[2] in cat_dict:
            cat_dict[row[2]]+=1
    alphasorted_dict = dict(sorted(cat_dict.items()))
    valsorted_dict=dict( sorted(cat_dict.items(),
                           key=lambda item: item[1],
                           reverse=True))
    
    

    categories=valsorted_dict.keys()
    amount=valsorted_dict.values()
    newamount=[]
    newcat=[]
    for x in amount:
        newamount.append(x)
    for x in categories:
        newcat.append(x)

    dictforplot={}
    dictforplot["Cat"]=newcat
    dictforplot["Amt"]=newamount


    plt.barh(newcat, newamount)
    plt.title('Types of Restaurants on South U')
    plt.xlabel('Restaurant Category')
    plt.ylabel('Amount')
    plt.show()

    return alphasorted_dict
        


   

#EXTRA CREDIT
def highest_rated_category(db_filename):#Do this through DB as well
    """
    This function finds the average restaurant rating for each category and returns a tuple containing the
    category name of the highest rated restaurants and the average rating of the restaurants
    in that category. This function should also create a bar chart that displays the categories along the y-axis
    and their ratings along the x-axis in descending order (by rating).
    """
    pass

#Try calling your functions here
def main():
    get_restaurant_data("South_U_Restaurants.db")
    barchart_restaurant_categories("South_U_Restaurants.db")
    pass

class TestHW8(unittest.TestCase):
    def setUp(self):
        self.rest_dict = {
            'name': 'M-36 Coffee Roasters Cafe',
            'category': 'Cafe',
            'building': 1101,
            'rating': 3.8
        }
        self.cat_dict = {
            'Asian Cuisine ': 2,
            'Bar': 4,
            'Bubble Tea Shop': 2,
            'Cafe': 3,
            'Cookie Shop': 1,
            'Deli': 1,
            'Japanese Restaurant': 1,
            'Juice Shop': 1,
            'Korean Restaurant': 2,
            'Mediterranean Restaurant': 1,
            'Mexican Restaurant': 2,
            'Pizzeria': 2,
            'Sandwich Shop': 2,
            'Thai Restaurant': 1
        }
        self.best_category = ('Deli', 4.6)

    def test_get_restaurant_data(self):
        rest_data = get_restaurant_data('South_U_Restaurants.db')
        self.assertIsInstance(rest_data, list)
        self.assertEqual(rest_data[0], self.rest_dict)
        self.assertEqual(len(rest_data), 25)

    def test_barchart_restaurant_categories(self):
        cat_data = barchart_restaurant_categories('South_U_Restaurants.db')
        self.assertIsInstance(cat_data, dict)
        self.assertEqual(cat_data, self.cat_dict)
        self.assertEqual(len(cat_data), 14)

    # def test_highest_rated_category(self):
    #     best_category = highest_rated_category('South_U_Restaurants.db')
    #     self.assertIsInstance(best_category, tuple)
    #     self.assertEqual(best_category, self.best_category)

if __name__ == '__main__':
    main()
    unittest.main(verbosity=2)
