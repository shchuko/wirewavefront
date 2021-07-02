#
#  Copyright (c) 2021, Vladislav Yaroshchuk <yaroshchuk2000@gmail.com>
#
#  SPDX-License-Identifier: BSD-2-Clause
#
from wirewavefront.primitives.vertex import Vertex


class Face:
    def __init__(self, vertexes: list = None):
        if vertexes is None:
            vertexes = list()
        self._vertexes = vertexes

    def add_vertex(self, v: Vertex):
        self._vertexes.append(v)

    def add_vertexes(self, v_list: list):
        self._vertexes += v_list

    def get_vertexes(self) -> list:
        return self._vertexes

    def __str__(self) -> str:
        return f"[{', '.join(map(str, self._vertexes))}]"
