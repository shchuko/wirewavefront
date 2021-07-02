#
#  Copyright (c) 2021, Vladislav Yaroshchuk <yaroshchuk2000@gmail.com>
#
#  SPDX-License-Identifier: BSD-2-Clause
#
class WavefrontWireframe:
    def __init__(self, faces, lines):
        self._faces = faces
        self._lines = lines

    def get_faces(self) -> list:
        return self._faces

    def get_lines(self) -> list:
        return self._lines
