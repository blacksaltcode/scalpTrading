import os
import sys
import warnings

def warn(*args, **kwargs):
    pass

warnings.warn = warn
warnings.simplefilter(action='ignore', category=FutureWarning)


sys.path.append(os.path.dirname(os.path.abspath('')))

from environments import TradingEnvironment
from exchanges.simulated import FBMExchange
from actions import DiscreteActionStrategy
from rewards import SimpleProfitStrategy

exchange = FBMExchange()
action_strategy = DiscreteActionStrategy()
reward_strategy = SimpleProfitStrategy()

env = TradingEnvironment(exchange=exchange,
                         action_strategy=action_strategy,
                         reward_strategy=reward_strategy)

obs = env.reset()
sell_price = 1e9
stop_price = -1

print('Initial portfolio: ', exchange.portfolio)

for i in range(1000):
    action = 0 if obs['close'] < sell_price else 18
    action = 19 if obs['close'] < stop_price else action
    
    if i == 0 or portfolio['BTC'] == 0:
        action = 16
        sell_price = obs['close'] + (obs['close'] / 50)
        stop_price = obs['close'] - (obs['close'] / 50)
    
    obs, reward, done, info = env.step(action)
    executed_trade = info['executed_trade']
    filled_trade = info['filled_trade']
    portfolio = exchange.portfolio
    
    print('Obs: ', obs)
    print('Reward: ', reward)
    print('Portfolio: ', portfolio)
    print('Trade executed: ', executed_trade.trade_type, executed_trade.price, executed_trade.amount)
    print('Trade filled: ', filled_trade.trade_type, filled_trade.price, filled_trade.amount)