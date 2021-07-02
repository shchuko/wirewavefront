#
#  Copyright (c) 2021, Vladislav Yaroshchuk <yaroshchuk2000@gmail.com>
#
#  SPDX-License-Identifier: BSD-2-Clause
#
from logging import Logger
from pathlib import Path

from wirewavefront.primitives.face import *
from wirewavefront.primitives.line import *
from wirewavefront.primitives.vertex import *
from wirewavefront.wireframe import WavefrontWireframe


class WavefrontParser:
    def __init__(self,
                 file_path: Path,
                 encoding: str = "utf-8",
                 logger: Logger = None):
        self.logger = logger

        self.line_generator = WavefrontParser._create_line_generator(file_path, encoding)
        self.values = None

        self.parsed_vertexes = []
        self.parsed_faces = []
        self.parsed_lines = []

        self.element_parsers_map = {method_name.split("_")[2]: getattr(self, method_name)
                                    for method_name in dir(self)
                                    if method_name.startswith("_parse_")}

    def parse(self):
        try:
            while True:
                if self.values is None:
                    self._next_line()

                if len(self.values) < 2 or self.values[0].startswith('#'):
                    self._skip_line()
                else:
                    self._get_element_parser(self.values[0])()
        except StopIteration:
            pass

    def get_wireframe(self) -> WavefrontWireframe:
        return WavefrontWireframe(self.parsed_faces, self.parsed_lines)

    @staticmethod
    def _create_line_generator(file_name: Path, encoding: str):
        with open(file_name, mode='r', encoding=encoding) as file:
            for line in file:
                yield line

    def _get_element_parser(self, element: str):
        return self.element_parsers_map.get(element, self._on_unimplemented_statement)

    def _on_unimplemented_statement(self):
        if self.logger is not None:
            self.logger.info(f"Unimplemented Wavefront format statement '{self.values[0]}'")
        self._skip_line()

    def _next_line(self):
        # Raises StopIteration if no lines left
        self.values = next(self.line_generator).split()

    def _skip_line(self):
        self.values = None

    def _skip_series(self, element_type: str):
        while True:
            try:
                self._next_line()
            except StopIteration:
                self._skip_line()
                break

            if self.values is None or self.values[0] != element_type:
                break

    def _parse_mtllib(self):
        self._skip_line()

    def _parse_o(self):
        self._skip_line()

    def _parse_v(self):
        self.parsed_vertexes += list(self.__parse_vertex_series())

    def __parse_vertex_series(self):
        while True:
            yield Vertex(x=float(self.values[1]), y=float(self.values[2]), z=float(self.values[3]))

            try:
                self._next_line()
            except StopIteration:
                self._skip_line()
                break

            if self.values is None or self.values[0] != "v":
                break

    def _parse_vt(self):
        self._skip_series("vt")

    def _parse_vn(self):
        self._skip_series("vn")

    def _parse_usemtl(self):
        self._skip_line()

    def _parse_f(self):
        self.parsed_faces += list(self.__parse_face_series())

    def __parse_face_series(self):
        while True:
            # Iterate over the face vertexes data
            # Collecting vertex indexes only
            # And mapping them to saved vertexes
            yield Face(list(self.parsed_vertexes[int(v_data.split('/')[0]) - 1] for v_data in self.values[1:]))

            try:
                self._next_line()
            except StopIteration:
                self._skip_line()
                break

            if self.values is None or self.values[0] != "f":
                break

    def _parse_l(self):
        while True:
            # Collect wavefront polyline segments as separate lines
            self.parsed_lines += list([Line(self.parsed_vertexes[int(self.values[i + 1].split('/')[0]) - 1],
                                            self.parsed_vertexes[int(self.values[i + 2].split('/')[0]) - 1])
                                       for i in range(len(self.values) - 2)])

            try:
                self._next_line()
            except StopIteration:
                self._skip_line()
                break

            if self.values is None or self.values[0] != "l":
                break
