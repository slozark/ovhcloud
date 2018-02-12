# -*- encoding: utf-8 -*-

class ArgumentError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class InternalError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)