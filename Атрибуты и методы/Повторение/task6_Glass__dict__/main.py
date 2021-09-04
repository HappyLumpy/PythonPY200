class Glass:
    def __init__(self, capacity_volume: [int, float], occupied_volume: [int, float]):
        self.capacity_volume = capacity_volume  # объем стакана
        self.occupied_volume = occupied_volume  # объем жидкости в стакане


if __name__ == "__main__":
    glass = Glass(200, 100)
