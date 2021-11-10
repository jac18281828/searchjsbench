import json
if __name__ == '__main__':
    with open('data/datadict.json', 'r') as datastream:
        filterlist = []
        datadict = json.load(datastream)
        for k,v in datadict.items():
            filter = None
            if isinstance(v, list):
                for i in range(1, len(v)+1):
                    filter = {
                        'name': k + str(i),
                        'filter': {k : v[:i]}
                    }
                    filterlist.append(filter)                    
            else:
                filter = {
                    'name': k,
                }
                filterlist.append(filter)
        print(json.dumps(filterlist, indent=4))

