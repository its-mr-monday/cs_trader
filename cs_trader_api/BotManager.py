from cs_trader_bot.bot import TradeBot, TradeBotException
from cs_trader_bot.botAuth import botAuth
import json, os

class BotManager:
    def __init__(self):
        self.bots = []
    
    
    
