
def make_folds(sampling, k):
    
    aux = list(sampling[int(parte*len(sampling)/k):int((parte+1)*len(sampling)/k)] for parte in range(k))
    return dict(zip(list(range(k)),aux))