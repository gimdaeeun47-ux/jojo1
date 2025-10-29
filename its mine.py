import csv

class ParkingZone:
    def __init__(self, floor, zone, remainum):
        self.floor = floor
        self.zone = zone
        self.remainum = int(remainum)

    def show(self):
        print(f"{self.floor}층 {self.zone}구역 → 남은 자리 {self.remainum}개")


def load_parking_data(filename):
    """CSV에서 주차 정보 불러오기"""
    zones = []
    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:
            zones.append(ParkingZone(row["floor"], row["zone"], row["remainum"]))
    return zones


def calculate_floor_summary(zones):
    """층별 총 잔여 자리 계산"""
    floor_summary = {}
    for z in zones:
        if z.floor not in floor_summary:
            floor_summary[z.floor] = 0
        floor_summary[z.floor] += z.remainum
    return floor_summary


def get_congestion_status(remain):
    """혼잡도 판단"""
    if remain == 0:
        return "만차"
    elif remain <= 3:
        return "혼잡"
    elif remain <= 6:
        return "보통"
    else:
        return "여유"


def show_parking_status(zones):
    """전체 구역 출력"""
    print("\n===== 구역별 주차 현황 =====")
    for z in zones:
        z.show()

def show_floor_summary(floor_summary):
    """층별 잔여 자리 + 혼잡도 출력"""
    print("\n===== 층별 주차 혼잡도 =====")
    for floor, remain in floor_summary.items():
        status = get_congestion_status(remain)
        print(f"{floor}층 → 총 잔여 자리: {remain}개 | 상태: {status}")

def main():
    filename = "parking.csv"
    zones = load_parking_data(filename)
    show_parking_status(zones)
    summary = calculate_floor_summary(zones)
    show_floor_summary(summary)

if __name__ == "__main__":
    main()
