import sys,json
from collections import OrderedDict

class Cardinality:

    def __init__(self, filename):
        with open(filename, 'r') as filestream:
            self.datadict = json.load(filestream)
        self.n_trans = len(self.datadict)
        self.carddict = {}


    def add_key(self, key, value):
        if key not in self.carddict:
            self.carddict[key] = set()
        self.carddict[key].add(value)


    def count_recursive(self, event, path = ""):
        for k, v in event.items():
            key = path + k.lower()
            if isinstance(v, dict):
                self.count_recursive(v, key + '.')
            elif isinstance(v, list):
                for entry in v:
                    if isinstance(entry, dict):
                        self.count_recursive(entry, key  + '.')
                    else:
                        self.add_key(key, entry)
            else:
                self.add_key(key, v)
                
    def count_members(self):
        for transaction in self.datadict:
            self.count_recursive(transaction)

    def cardinality(self):
        cardinality = OrderedDict()
        for k, v in sorted(self.carddict.items(), key=lambda item: len(item[1])):
            cardinality[k] = min(self.n_trans, len(v))
        return cardinality

if __name__  == '__main__':
    for file in sys.argv[1:]:
        card = Cardinality(file)
        card.count_members()
        cardinality = card.cardinality()
        print(json.dumps(cardinality, indent=4, sort_keys=False))

        datadict = card.carddict
        for k,v in cardinality.items():
            if v > 10:
                del datadict[k]
            else:
                datadict[k] = list(datadict[k])

        print(json.dumps(datadict, indent=4, sort_keys=True))
    
