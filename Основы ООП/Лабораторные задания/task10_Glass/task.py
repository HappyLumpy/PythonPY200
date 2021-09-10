class Glass:
    def __init__(self, capacity_volume: [int, float], occupied_volume: [int, float], material: str):
        self.capacity_volume = capacity_volume  # объем стакана
        self.occupied_volume = occupied_volume  # объем жидкости в стакане
        self.material = material

    def get_material(self):
        return self.material

    def __str__(self):
        return f"Стакан объемом {self.capacity_volume}, занятый объем {self.occupied_volume}, материал {self.material}"


if __name__ == "__main__":
    glass_1 = Glass(100, 1, "steel")
    print(glass_1)
