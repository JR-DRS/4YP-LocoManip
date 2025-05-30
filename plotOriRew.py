import matplotlib.pyplot as plt
import pandas as pd
from helpfulFuncs import dropAfterX
import numpy as np




folder1='exponentialNoMovement'
#folder2='0.7CircleBlindp2'
#folder3='HistoryLen6Var-5,10'

drop=10000

posError1=pd.read_csv(f'{folder1}/oriRew.csv')
posError1=dropAfterX(posError1,drop)

#posError2=pd.read_csv(f'{folder2}/posError.csv')
#posError2=dropAfterX(posError2,drop+10000)

#posError3=pd.read_csv(f'{folder3}/posError.csv')
#posError3=dropAfterX(posError3,drop)

fig,ax=plt.subplots()

ax.plot(posError1['Step'],posError1[f'{folder1} - Episode_Reward/oriRew'],color='b')
#ax.plot(posError2['Step'],posError2[f'{folder2} - Metrics/targetPosition/error_pos_2d'],color='b')
#ax.plot(posError2['Step'],posError3[f'HistoryLen6-5,10 - Metrics/targetPosition/error_pos_2d'],label='Length 6')

#ax.set_yscale('log')

ax.set_xlabel('Step')
ax.set_ylabel('Orientation reward')
ax.set_title('Evolution of orientation reward across steps')
#ax.legend()

fig.savefig(f'{folder1}/MetricGraph.png')