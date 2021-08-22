import pickle
import matplotlib.pyplot as plt 

def save_obj(obj, name ):
    with open('./board/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open('./board/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)
    
# PLOTTING MATPLOTLIB FUNCTIONS (PROBABLY OLD)
'''Saves a single plot(x,y,'-o') as an image, used to plot the total counts among all chambers'''
def plot1(X,Y,filename,title):
    fig1, (ax0) = plt.subplots(nrows=1, ncols=1, figsize=(40, 16))
    
    ax0.plot(X,Y1,'-o',lw=4,ms=16)
    ax0.set_title(title,loc='left',fontdict={'fontsize': 50},pad=30)
    ax0.tick_params(axis='x', labelsize=30)
    ax0.tick_params(axis='y', labelsize=30)
    fig1.savefig('./imgs/'+filename+'.jpg')

'''Saves 4 plot(x,y,'-o') as an image, used to plot the total counts for each chamber'''
def plot4(X,YS,filename):
    fig2, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(18, 8))
    axs = [ax1, ax2, ax3, ax4]
    for i, chamber in enumerate(["Chamber_1", "Chamber_2", "Chamber_3", "Chamber_4"]):
        axs[i].plot(X,YS[i],'-o',color='royalblue')
        axs[i].set_title('Total counts of events: CHAMBER '+str(i+1),loc='left',fontdict={'fontsize': 20},pad=30)
    fig2.subplots_adjust(hspace=.5)
    fig2.savefig('./imgs/'+filename+'.jpg')
    
def hist4(counts,bins,filename):
    fig3, ((hx1, hx2), (hx3, hx4), (hx5, hx6), (hx7,hx8)) = plt.subplots(nrows=4, ncols=2, figsize=(20, 14))
    hxs = [[hx1,hx2],[hx3,hx4],[hx5,hx6],[hx7,hx8]]
    for i, chamber in enumerate(["Chamber_1", "Chamber_2", "Chamber_3", "Chamber_4"]):
        hxs[i][0].hist(counts[2*i],bins[2*i])
        hxs[i][0].set_title('Histogram 1',loc='left',fontdict={'fontsize': 20},pad=10)
        hxs[i][0].tick_params(axis='y', labelsize=10)
        hxs[i][0].tick_params(axis='x', labelsize=10)
        
        hxs[i][1].hist(counts[2*i+1],bins[2*i+1])
        hxs[i][1].set_title('Histogram 2',loc='left',fontdict={'fontsize': 20},pad=10)
        hxs[i][1].tick_params(axis='y', labelsize=10)
        hxs[i][1].tick_params(axis='x', labelsize=10)
        
        fig3.text(0.5,0.95-i/4.6, "Chamber "+str(i+1), ha="center", va="top", fontsize=24)
    fig3.subplots_adjust(hspace=1)
    fig3.savefig('./imgs/'+filename+'.jpg')