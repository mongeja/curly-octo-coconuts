#spots_model.py
import math
import random

class Spot:
    def __init__(self, center: (float, float), radius: float):
        self._center_x. self._center_y = center
        self._radius = random.random() * 0.09 + 0.01

        self._delta_x = random.random() * 0.025 - 0.0125
        self._delta_y = random.random() * 0.025 - 0.0125
    
    def center(self) -> (float, float):
        return (self._center_x, self._center_y)

    def radius(self) -> float:
        return self._radius

    def move(self) -> None:
        self._center_x += self._delta_x
        self._center_y += self._delta_y

    def contains(self, frac_x: float, frac_y: float) -> bool:
        diff_x = frac_x - self._center_x
        diff_y = frac_y - self._center_y

        return math.sqrt(diff_x * diff_x + diff_y * diff_y) <= self._radius



class SpotsState:
    def __init__(self):
        self._spots = []
    
    def all_spots(self) -> [Spot]:
        return self._spots

    def handle_click(self, frac_x: float, frac_y: float) -> None:
        for spot in self._spots:
            if spot.contains(frac_x, frac_y):
                self.spots.remove(spot)
        
        new_spot = Spot((frac_x, frac_y), 0.05)
        self._spots.append(new_spot)

    def move_all_spots(self) -> None:
        for spots in self._spots:
            pass
        
