import pandas
from fpdf import FPDF


df = pandas.read_csv("articles.csv", dtype={"id":str})


class Item:
    def __init__(self, id):
        self.item_id = id
        self.name = df.loc[df["id"] == self.item_id, "name"].squeeze()
        self.price = df.loc[df["id"] == self.item_id, "price"].squeeze()

    def purchase(self):
        df.loc[df["id"] == self.item_id, "in stock"] -= 1
        df.to_csv("articles.csv", index=False)

    def in_stock(self):
        items = df.loc[df["id"] == self.item_id, "in stock"].squeeze()
        return items


class Receipt:
    def __init__(self, item):
        self.item = item

    def generate(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt {self.item.item_id}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.item.name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.item.price}", ln=1)

        pdf.output("receipt.pdf")

print(df)
item_id = input("Enter the id of the item you want to purchase: ")
item = Item(item_id)
if item.in_stock():
    item.purchase()
    receipt = Receipt(item = item)
    print(receipt.generate())
