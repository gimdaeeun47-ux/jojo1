zone_list = []
class parking_zone:
    count = 0

    def __init__(self, zone, full, trait):
        self.zone = zone
        self.full = full
        self.trait = trait


    @classmethod
    def count_parked(cls):
        cls.count += 1
        print(f"잔여 구역{cls.count}")

for i in range(10):
    zone = parking_zone("A"+str(i+1), 0, 0)
    zone_list.append(zone)

zone_list[0].
