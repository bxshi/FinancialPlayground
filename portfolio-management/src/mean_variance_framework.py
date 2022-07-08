import numpy as np
import yfinance as yf
import requests_cache

session = requests_cache.CachedSession('yfinance.cache')


edv = yf.Ticker("EDV", session=session)
edv_hist = edv.history(period="10y")

voo = yf.Ticker("VOO", session=session)
voo_hist = voo.history(period="10y")

qqq = yf.Ticker("QQQ", session=session)
qqq_hist = qqq.history(period="10y")

print(np.corrcoef(np.stack([edv_hist.Close, voo_hist.Close, qqq_hist.Close], axis=0)))