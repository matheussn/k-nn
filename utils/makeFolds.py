
def make_folds(sampling, k):
    aux = [sampling[int(part*len(sampling)/k):int((part+1)*len(sampling)/k)] for part in range(k)]
    return dict(zip(list(range(k)), aux))
