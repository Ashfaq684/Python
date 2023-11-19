from item import Item
from phone import Phone

# Item.instantiate_from_csv()
# print(Item.all)

item1 = Item("MyItem", 750)
# item1.name = "OtherItem"
# item1._name = "OtherItem"

# print(item1.read_only_name)
# item1.read_only_name = "BBB"
# print(item1.read_only_name)

# item1.name = "OtherItem"
# print(item1.name)

item1.apply_increment(0.2)
print(item1.price)