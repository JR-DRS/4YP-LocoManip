import matplotlib.pyplot as plt
import pandas as pd
from helpfulFuncs import dropAfterX
import numpy as np




folder1='VariableNoHist'
folder2='HistoryLen4-5,10'
folder3='HistoryLen6-5,10'
#folder4='OriExp10Lin2D10'

drop=10000

posError1=pd.read_csv(f'{folder1}/posError.csv')
#posError1['Step']=posError1['Step']-8150
posError1=dropAfterX(posError1,drop)

'''
headError1=pd.read_csv(f'{folder1}/headError.csv')
headError1['Step']=headError1['Step']-8150
headError1=dropAfterX(headError1,drop)
'''
posError2=pd.read_csv(f'{folder2}/posError.csv')
posError2['Step']=posError2['Step']-20000
posError2=dropAfterX(posError2,drop)
'''
headError2=pd.read_csv(f'{folder2}/headError.csv')
headError2['Step']=headError2['Step']-20000
headError2=dropAfterX(headError2,drop)
'''

posError3=pd.read_csv(f'{folder3}/posError.csv')
posError3=dropAfterX(posError3,drop)
'''
headError3=pd.read_csv(f'{folder3}/headError.csv')
headError3=dropAfterX(headError3,drop)

posError4=pd.read_csv(f'{folder4}/posError.csv')
posError4=dropAfterX(posError4,drop)

headError4=pd.read_csv(f'{folder4}/headError.csv')
headError4=dropAfterX(headError4,drop)
'''


fig,ax=plt.subplots()

ax.plot(posError1['Step'],posError1[f'AnymalD-ArmLess-Variable4 - Metrics/targetPosition/error_pos_2d'])
#ax.plot(posError2['Step'],posError2[f'{folder2} - Metrics/targetPosition/error_pos_2d'],label='Length 4')
#ax.plot(posError3['Step'],posError3[f'{folder3} - Metrics/targetPosition/error_pos_2d'],label='Length 6')
#ax.plot(posError4['Step'],posError4[f'{folder4} - Metrics/targetPosition/error_pos_2d'],color='orange',label='Experiment 3')

#ax.set_yscale('log')

ax.set_xlabel('Step')
ax.set_ylabel('Position Error/m')
ax.set_title('Evolution of the payload position error across steps')
ax.legend()

fig.savefig(f'{folder1}/triplePosError.png')
'''
fig,ax=plt.subplots()

ax.plot(headError1['Step'],headError1[f'{folder1} - Metrics/targetPosition/error_heading'],color='r',label='Experiment 4')
ax.plot(headError2['Step'],headError2[f'{folder2} - Metrics/targetPosition/error_heading'],color='orange',label='Experiment 5')
#ax.plot(headError3['Step'],headError3[f'{folder3} - Metrics/targetPosition/error_heading'],color='r')
#ax.plot(headError4['Step'],headError4[f'{folder4} - Metrics/targetPosition/error_heading'],color='orange',label='Experiment 3')




ax.set_xlabel('Step')
ax.set_ylabel('Heading Error/rad')
ax.set_title('Evolution of the payload heading error across steps')
ax.legend()

fig.savefig(f'{folder1}/headError.png')
'''