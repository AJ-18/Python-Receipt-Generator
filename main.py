import pandas

df = pandas.read_csv("articles.csv")


class Item:
    def __init__(self, id):
        self.item_id = id





class Receipt:
    pass


print(df)
item_id = input("Enter the id of the item you want to purchase: ")
item = Item(item_id)
