element = lambda value, next_: {'value': value, 'next': next_}
to_string = lambda head: '' if head is None \
        else str(head['value']) + ' ' + to_string(head['next'])

values = element('abra', element('cad', element('abra', None)))
print(values)
print(to_string(values))