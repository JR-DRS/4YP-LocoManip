import matplotlib.pyplot as plt
import pandas as pd
from helpfulFuncs import dropAfterX

from matplotlib.legend_handler import HandlerTuple

folder1='exponentialNoMovement'
#folder2='0.7CircleBlindp2'
#folder3='HistoryLen6Var-5,10'

drop=10000

bot2payload1=pd.read_csv(f'{folder1}/bot2payload.csv')
payload2target1=pd.read_csv(f'{folder1}/payload2target.csv')

#bot2payload2=pd.read_csv(f'{folder2}/bot2payload.csv')
#payload2target2=pd.read_csv(f'{folder2}/payload2target.csv')

#bot2payload3=pd.read_csv(f'{folder3}/bot2payload.csv')
#payload2target3=pd.read_csv(f'{folder3}/payload2target.csv')

bot2payload1=dropAfterX(bot2payload1,drop)
payload2target1=dropAfterX(payload2target1,drop)

#bot2payload2=dropAfterX(bot2payload2,drop)
#payload2target2=dropAfterX(payload2target2,drop)

#bot2payload3=dropAfterX(bot2payload3,drop)
#payload2target3=dropAfterX(payload2target3,drop)


bot2payload1[f'AnymalD-ArmLess-Variable4 - Episode_Reward/bot_2_payload']=bot2payload1[f'AnymalD-ArmLess-Variable4 - Episode_Reward/bot_2_payload']*1.25
payload2target1[f'AnymalD-ArmLess-Variable4 - Episode_Reward/payload_2_target']=payload2target1[f'AnymalD-ArmLess-Variable4 - Episode_Reward/payload_2_target']*1.25

fig,ax=plt.subplots()

ax.plot(bot2payload1['Step'],bot2payload1[f'AnymalD-ArmLess-Variable4 - Episode_Reward/bot_2_payload'],color='b')
ax.plot(payload2target1['Step'],payload2target1[f'AnymalD-ArmLess-Variable4 - Episode_Reward/payload_2_target'],color='r')

#ax.plot(bot2payload2['Step'],bot2payload2[f'{folder2} - Episode_Reward/bot_2_payload'],color='b')
#ax.plot(payload2target2['Step'],payload2target2[f'{folder2} - Episode_Reward/payload_2_target'],color='r')

#ax.plot(bot2payload3['Step'],bot2payload3[f'HistoryLen6-5,10 - Episode_Reward/bot_2_payload'],label='Length 6 bot2payload')
#ax.plot(payload2target3['Step'],payload2target3[f'HistoryLen6-5,10 - Episode_Reward/payload_2_target'],label='Length 6 payload2target')




ax.axhline(5,0,1)
ax.axhline(10,0,1,c='r')

ax.set_xlabel('Step')
ax.set_ylabel('Reward')
ax.set_title('Evolution of reward across steps')
ax.legend()

fig.savefig(f'{folder1}/RewardGraph.png')