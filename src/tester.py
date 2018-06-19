import csv

class balls:

    def __init__(self):
        self.location = [0, 0]

    def bla(self):
        print(self.location[0])

csv_file = "world/room_text.csv"
map = list(csv.reader(open(csv_file)))
for i in map:
    print(i)