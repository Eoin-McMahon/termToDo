from termcolor import colored
from tabulate import tabulate
from utils import Utils
from table import Table
import os

class termToDo(object):
    
    def __init__(self, items, done, table_headers):
        self.items = items
        self.table_headers = table_headers
        self.done = done
        self.utils = Utils()

    def main(self):
        table = Table(self.items, self.done, self.table_headers)
        table.draw_table()
        command = None
        options = {
           1 : table.add,
           2 : table.mark_done,
           3 : table.clear,
           4 : table.alter,
           5 : table.delete,
        }

        while(True):
            command = int(self.utils.showInputField())
            if (command == 6):
                return
            options[command]()

        return
if __name__ == "__main__":

    utils = Utils()
    items = utils.load_items()[0]
    done = utils.load_items()[1]
    termList = termToDo(items, done, ["id", "TO DO LIST"])
    termList.main()
