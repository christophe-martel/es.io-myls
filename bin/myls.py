# coding: utf-8
"""Simple module to implements subject described in readme.md

See readme.
"""
import os
import logging
from typing import Set
import humanize


class HumanReadableByte:
    """Utility class to convert interger bytes to human readable string"""
    available = ['auto', 'B', 'kB', 'MB', 'GB']

    defaultUnit = 'auto'

    def __init__(self, unit=None):
        unit = unit if unit is not None else HumanReadableByte.defaultUnit
        if not unit in HumanReadableByte.available:
            raise Exception(
                'Unknown unit "{}".'
                'Available values : {}'.format(unit, HumanReadableByte.available))
        self.__unit = unit

    def convert(self, value: int)->str:
        """ convert bytes from integer to string using unit"""
        if self.__unit == 'auto':
            result = humanize.naturalsize(value)
            logging.debug(
                'apply human readable bytes(mode=humanize), value=%s result=%s',
                value,
                result
            )
            return result

        if value < 1:
            logging.debug('apply human readable bytes(mode=self), value < 1')
            return '0{}'.format(self.__unit)

        result = HumanReadableByte.apply(value, self.__unit, HumanReadableByte.available[1:])
        logging.debug('apply human readable bytes(mode=self), value=%s result=%s', value, result)
        return result

    @staticmethod
    def apply(value: int, unit: str, units: Set[str] = None) ->str:
        """ Returns a human readable string reprentation of bytes"""
        units = units if units is not None else HumanReadableByte.available[1:]

        if not units:
            return str(value)

        if len(units) < 2:
            return str(value) + units[0]

        if unit == units[0]:
            return str(value) + units[0]

        logging.debug('apply human readable bytes, value=%s, unit=%s, units=%s', value, unit, units)

        if value < 1024:
            return str(value) + units[0]

        return  HumanReadableByte.apply(value >> 10, unit, units[1:])

    def __str__(self):
        return '{}'.format(self.__unit)

    def __eq__(self, other):
        """Overrides the basic EQ implementation

        :param other: (object) The object we want self to be compared with
        :return: (bool) True if it's the same object, False otherwise
        """
        if isinstance(self, other.__class__) is False:
            return False

        return str(self) == str(other)

class MyLsEntry:
    """embed filepath, size and type in Set """
    FILE = 'file'
    DIR = 'dir'

    def __init__(self, file: str, type_of_file: str, size=None):
        self.file = file
        self.type_of_file = type_of_file
        self.size = size

    def __str__(self):
        return '[{}]\t{}{}'.format(
            "f" if self.FILE == self.type_of_file else "d",
            self.file,
            '\t({})'.format(self.size) if self.FILE == self.type_of_file else "")

    def __eq__(self, other):
        """Overrides the basic EQ implementation

        :param other: (object) The object we want self to be compared with
        :return: (bool) True if it's the same object, False otherwise
        """
        if isinstance(self, other.__class__) is False:
            return False

        if  self.file != other.file:
            return False

        if  self.type_of_file != other.type_of_file:
            return False

        return True


class MyLs:
    """embed  a Set of MyLsEntry to represent files (regular and dir) in a directory """
    def __init__(self, humanReadableByte):
        self.__human_readable_byte = humanReadableByte

    def list(self, directory: str) ->Set[MyLsEntry]:
        """Get file list from directory

        :return: Set[MyLsEntry]
        """

        result = map(
            lambda x:
            MyLsEntry(
                x,
                MyLsEntry.DIR if os.path.isdir(x) else MyLsEntry.FILE,
                None if os.path.isdir(x) else self.__human_readable_byte.convert(os.path.getsize(x))
            ),
            map(lambda x: os.path.join(directory, x), os.listdir(directory)))


        return result


    def __str__(self):
        return '{}'.format(self.__human_readable_byte)

    def __eq__(self, other):
        """Overrides the basic EQ implementation

        :param other: (object) The object we want self to be compared with
        :return: (bool) True if it's the same object, False otherwise
        """
        if isinstance(self, other.__class__) is False:
            return False

        return str(self) == str(other)
