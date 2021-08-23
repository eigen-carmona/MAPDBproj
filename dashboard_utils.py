import pickle
import matplotlib.pyplot as plt 

nullmessage = {'Total Count' : 0, 'Index': 0,
               'Chamber_1' : {'Count': 0, 'Hist_1' : {'Bins' : [0,1], 'Counts': [0,0] },
                                          'Hist_2' : {'Bins' : [0,1], 'Counts': [0,0] }},
               'Chamber_2' : {'Count': 0, 'Hist_1' : {'Bins' : [0,1], 'Counts': [0,0] },
                                          'Hist_2' : {'Bins' : [0,1], 'Counts': [0,0] }},
               'Chamber_3' : {'Count': 0, 'Hist_1' : {'Bins' : [0,1], 'Counts': [0,0] },
                                          'Hist_2' : {'Bins' : [0,1], 'Counts': [0,0] }},
               'Chamber_4' : {'Count': 0, 'Hist_1' : {'Bins' : [0,1], 'Counts': [0,0] },
                                          'Hist_2' : {'Bins' : [0,1], 'Counts': [0,0] }}}

def save_obj(obj, name ):
    with open('./board/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    try:
        with open('./board/' + name + '.pkl', 'rb') as f:
            return pickle.load(f)
    except:
        return nullmessage
    
def getmaxcount(message,numhist):
    allmax = 0
    for i in range(4):
        chmax = max(message['Chamber_'+str(i+1)]['Hist_'+str(numhist)]['Counts'])
        if chmax > allmax:
            allmax = chmax
        if allmax == 0:
            allmax = 1
    return(allmax)