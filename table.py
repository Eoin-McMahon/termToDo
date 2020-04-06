from tabulate import tabulate
from utils import Utils
import time

class Table():
    def __init__(self, table_items, done_items, table_headers):
        self.headers = table_headers
        self.items = table_items
        self.done = done_items
        self.utils = Utils()
        return

    def draw_table(self):
        self.utils.store_items(self.items, self.done)
        self.utils.clear_screen()
        table_contents = [(i, elem) for i, elem in enumerate(self.items)]
        print(tabulate(table_contents, headers=self.headers))
        print("\nEnter a Command to interact:\n1) ADD\t\t2) Mark Done \t\t3) Clear Done\n4) Alter\t5) Delete\t\t6) Exit")

    def add(self):
        print("Enter Text To ADD:")
        text = self.utils.showInputField()
        self.items.append(text)
        self.draw_table()

    def mark_done(self):
        print("Enter Item ID:")
        item_id = int(self.utils.showInputField())
        while (item_id > len(self.items) + 1):
            print("No item in list with that ID, try again")
            item_id = int(self.utils.showInputField())


        done_item = self.items[item_id] 
        if done_item not in self.done:
            self.items[item_id] = self.utils.strike(done_item)
            self.done.append(self.items[item_id])
        self.draw_table()

    def clear(self):
        list_items = [item for item in self.items if item not in self.done]
        self.items = list_items
        self.draw_table()
    
    def alter(self):
        print("Enter Item ID:")
        item_id = int(self.utils.showInputField())
        text = self.items[item_id]
        replacement = input("\r%s >> " % text)
        self.items[item_id] = replacement
        self.draw_table()

    def delete(self):
        print("Enter Item ID or * for ALL")
        text = self.utils.showInputField()
        if (text == "*"):
            self.items = []

        else:
            item_id = int(text)
            try:
                del self.items[item_id]
            except IndexError:
                self.delete()

        self.draw_table()