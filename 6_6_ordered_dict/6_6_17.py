from collections import OrderedDict

data = OrderedDict([('key3', 'value3'), ('key2', 'value2'), ('key1', 'value1')])
print(OrderedDict(reversed(data.items())))