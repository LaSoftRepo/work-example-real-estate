# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from admin2.models import Counters


def counter(request):
    counters = Counters.get_solo()
    return {
        'counter_1': counters.counter_1,
        'counter_2': counters.counter_2,
        'counter_3': counters.counter_3,
        'counter_4': counters.counter_4
    }