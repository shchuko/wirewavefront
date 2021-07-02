#
#  Copyright (c) 2021, Vladislav Yaroshchuk <yaroshchuk2000@gmail.com>
#
#  SPDX-License-Identifier: BSD-2-Clause
#
class Vertex:
    def __init__(self, x: float, y: float, z: float):
        self.cords = x, y, z

    def get_x(self) -> float:
        return self.cords[0]

    def get_y(self) -> float:
        return self.cords[1]

    def get_z(self) -> float:
        return self.cords[2]

    def to_tuple(self) -> tuple:
        return self.cords

    def __str__(self) -> str:
        return self.to_tuple().__str__()

