import matplotlib.pyplot as plt
import pandas as pd
from helpfulFuncs import dropAfterX
import numpy as np

folder1='VariableNoHist'
#folder2='HistoryLen4Var-5,10'
#folder3='HistoryLen6Var-5,10'

drop=700



baseCon1=pd.read_csv(f'{folder1}/baseContact.csv')
baseCon1=dropAfterX(baseCon1,drop)

#baseCon2=pd.read_csv(f'{folder2}/baseContact.csv')
#baseCon2=dropAfterX(baseCon2,drop)

#baseCon3=pd.read_csv(f'{folder3}/baseContact.csv')
#baseCon3=dropAfterX(baseCon3,drop)


fig,ax=plt.subplots()

ax.plot(baseCon1['Step'],baseCon1[f'AnymalD-ArmLess-Variable4 - Episode_Termination/base_contact'])
#ax.plot(baseCon2['Step'],baseCon2[f'HistoryLen4-5,10 - Episode_Termination/base_contact'],label='Length 4')
#ax.plot(baseCon3['Step'],baseCon3[f'HistoryLen6-5,10 - Episode_Termination/base_contact'],label='Length 6')


ax.set_xlabel('Step')
ax.set_ylabel('Instances of failure through falling')
ax.set_title('Evolution of the number of base contact failures across steps')

fig.savefig(f'{folder1}/baseContactGraph.png')