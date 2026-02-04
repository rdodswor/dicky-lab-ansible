#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Custom text formatting filters for Ansible templates"""

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

def ljust(text, width, fillchar=' '):
    """Left-justify text in a field of given width
    
    Args:
        text: Text to justify
        width: Total width of field
        fillchar: Character to pad with (default: space)
    
    Returns:
        Left-justified string
    """
    return str(text).ljust(int(width), fillchar)

def rjust(text, width, fillchar=' '):
    """Right-justify text in a field of given width"""
    return str(text).rjust(int(width), fillchar)

def center(text, width, fillchar=' '):
    """Center text in a field of given width"""
    return str(text).center(int(width), fillchar)

class FilterModule(object):
    """Ansible filter plugin"""
    
    def filters(self):
        """Return dictionary of filter name -> filter function"""
        return {
            'ljust': ljust,
            'rjust': rjust,
            'center': center,
        }
