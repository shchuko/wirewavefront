#
#  Copyright (c) 2021, Vladislav Yaroshchuk <yaroshchuk2000@gmail.com>
#
#  SPDX-License-Identifier: BSD-2-Clause
#
from .wavefront_parse_exception import WavefrontParseException


class UnimplementedStatementException(WavefrontParseException):
    pass
