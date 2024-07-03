# Does post processing of data
def dataCleaning(data):
    del data['data-options']['json-url']
    return data