# -*- coding: utf-8 -*-.
# Provinces du Canada

import collections

provinces = {
    'Quebec': 'QC',
    'Ontario': 'ON',
    'Nova Scotia': 'NS',
    'New Bronswick': 'NB',
    'Manitoba': 'MB',
    'British Colombia': 'BC',
    'Prince Edward Island': 'PE',
    'Saskatchewan': 'SK',
    'Alberta': 'AB',
    'New Found Land': 'NL'
}

provinces = collections.OrderedDict(provinces)
print provinces
