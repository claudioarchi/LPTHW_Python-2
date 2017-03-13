# Provinces du Canada

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

cities = {
    'QC': 'Quebec city',
    'ON': 'Toronto',
    'BC': 'Vancouver'
}

# Adding keys and values to cities dict
cities['NB'] = 'Saint John'
cities['AB'] = 'Calgary'

# print some provinces
print ("-|-" * 10)
print "Quebec est abrv.: ", provinces['Quebec']
print "Manitoba est abrv.: ", provinces['Manitoba']
print "the city of QC is: ", cities['QC']
print "And its abbreviation is: ", provinces['Quebec']
print "the city of BC is: ", cities['BC']

# print every city in province
print ("-|-" * 10)
for provinces, abbrev in provinces.items():
    print ("_%s is abbreviated: %s" % (provinces, abbrev))


print ("-|-" * 10)
for abbrev, cities in cities.items():
    print ("La ville de %s est: %s" % (abbrev, cities))
