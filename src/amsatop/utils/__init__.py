"""
This module contains logic for making you easier to implement amsatop
"""

from amsatop.utils.stat_file import StatFile, get_stat_file_from_path
from amsatop.utils.status_file import StatusFile, get_status_file_from_path

__all__ = ["StatusFile", "StatFile", "get_status_file_from_path", "get_stat_file_from_path"]