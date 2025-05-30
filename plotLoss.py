import matplotlib.pyplot as plt
import pandas as pd
from helpfulFuncs import dropAfterX
import numpy as np




folder1='exponentialNoMovement'
#folder2='0.7CircleBlindp2'
#folder3=''

drop=10000

loss1=pd.read_csv(f'{folder1}/loss.csv')
loss1=dropAfterX(loss1,drop)
loss1=loss1.drop(loss1[loss1[f'{folder1} - Loss/value_function']>2].index)

#loss2=pd.read_csv(f'{folder2}/loss.csv')
#loss2=dropAfterX(loss2,drop+10000)
#loss2=loss2.drop(loss2[loss2[f'{folder2} - Loss/value_function']>1].index)

#loss3=pd.read_csv(f'{folder3}/loss.csv')
#loss3=dropAfterX(loss3,18750)


fig,ax=plt.subplots()

ax.plot(loss1['Step'],loss1[f'{folder1} - Loss/value_function'],color='b')
#ax.plot(loss2['Step'],loss2[f'{folder2} - Loss/value_function'],color='b')
#ax.plot(loss3['Step'],loss3[f'1Ball1BlockID - Loss/value_function'],'r',label='1Ball1BlockID')



ax.plot()


ax.set_yscale('log')
ax.set_xlabel('Step')
ax.set_ylabel('Loss/Value function')
ax.set_title('Evolution of the loss of the value function across steps')
ax.legend()
fig.savefig(f'{folder1}/lossGraph.png')