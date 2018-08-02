#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Any
from typing import Dict
from typing import Tuple


class TraitletSplitter(object):
    """
    {
      'owner': object,  # The HasTraits instance
      'new': 6,         # The new value
      'old': 5,         # The old value
      'name': "foo",    # The name of the changed trait
      'type': 'change', # The event type of the notification, usually 'change'
    }
    """
    @staticmethod
    def split(change: Dict[str, Any]) -> Tuple[Any, Any, Any]:
        return change["owner"], change["old"], change["new"]
