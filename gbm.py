#!/usr/bin/env python3

import sys
import numpy as np
import pandas as pd
import seaborn as sns
import scipy as sp
import matplotlib.pyplot as plt
from download import download

np.set_printoptions(suppress=True)

def gbm(dat, look_back="full", N=100, epoch=1000) -> int:
    look_back_options = {"full": 1,
                         "1yr": dat.shape[0] - 240,
                         "6m": dat.shape[0] - 120,
                         "3m": dat.shape[0] - 60}
    returns = []
    for t in range(look_back_options[look_back], dat.shape[0]):
        returns.append((dat["adjClose"][t] - dat["adjClose"][t-1]) / dat["adjClose"][t-1])
    returns = np.array(returns)

    s0 = dat["adjClose"].iloc[-1]
    mu = returns.mean()
    sigma = np.std(returns)
    drift = mu + 0.5 * sigma**2

    sample_path = []
    for e in range(epoch):
        shock = np.random.normal(0, 1, N)
        brownian = np.zeros(N+1)
        brownian[1:] = shock
        for t in range(1, N+1):
            brownian[t] += brownian[t-1]
        
        path = np.zeros(N+1)
        path[0] = s0
        for t in range(1, N+1):
            path[t] = s0 * np.exp(drift * t + sigma * brownian[t])
        sample_path.append(path)
    
    sample_path = np.array(sample_path)

    prices = sample_path.flatten()
    prices = prices[prices != s0]

    up = sum([price > s0 for price in prices]) / prices.shape[0]
    return up

if __name__ == "__main__":
    ticker = sys.argv[1]
    apikey = open("apikey", "r").readline()
    download(ticker, apikey)

    dat = pd.read_csv("./data/{}.csv" .format(ticker))
    dat = dat.loc[::-1].reset_index().drop(columns=["index"])

    sim = []
    for t in range(dat.shape[0] - 240):
        p = gbm(dat[:240+t], "6m")
        print("t={}: p(s > s_t)={}" .format(t, p))
        sim.append(p)
    
    plt.subplot(2, 1, 1)
    plt.plot(sim)
    plt.subplot(2, 1, 2)
    plt.plot(dat["adjClose"][240:])

    plt.savefig("gbm.png")