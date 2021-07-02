#
#  Copyright (c) 2021, Vladislav Yaroshchuk <yaroshchuk2000@gmail.com>
#
#  SPDX-License-Identifier: BSD-2-Clause
#
from wirewavefront.primitives.vertex import Vertex


class Line:
    def __init__(self, v_start: Vertex, v_end: Vertex):
        self._v_start = v_start
        self._v_end = v_end

    def get_start(self) -> Vertex:
        return self._v_start

    def get_end(self) -> Vertex:
        return self._v_end

    def __str__(self) -> str:
        return f"[{self._v_start}, {self._v_end}]"
