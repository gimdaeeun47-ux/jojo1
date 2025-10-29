import csv

total_empty = 0

class parking_zone:
    def __init__(self, zone, empty):
        global total_empty

        self.zone = zone 
        self.empty = empty
        total_empty += empty   

    def show(self):
        global total_empty

        print(f"{self.zone}에 {self.empty}개의 자리가 남아 있습니다.")
        print(f"전체 잔여 자리는 {total_empty}곳 입니다.")

zoneA = parking_zone("A", 0)
zoneA.show()

zoneB = parking_zone("B", 3)
zoneB.show()

zoneC = parking_zone("C", 7)
zoneC.show()