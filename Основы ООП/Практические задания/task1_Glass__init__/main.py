class Glass:
    def __init__(self, capacity_volume: [int, float], occupied_volume: [int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError()
        if capacity_volume <= 0:
            raise ValueError()
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume


if __name__ == "__main__":
    glass_1 = Glass(500, 0)
    print(glass_1)
    glass_2 = Glass(800, 500)
    print(glass_2)

    glass_3 = Glass('-200', 0)
    print(glass_3)
