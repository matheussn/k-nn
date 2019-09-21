
def make_Folds(sampling, k):
    
    aux = list(sampling[ int(parte*len(sampling)/k):int((parte+1)*len(sampling)/k) ] for parte in range(k))
    dic = dict( zip(list(range(k)), aux )) 
    
    return dic   