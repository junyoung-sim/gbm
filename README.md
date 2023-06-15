# Geometric Brownian Motion (GBM)

Geometric Brownian Motion is a stochastic process that models a randomly varying quantity following a Brownian motion with drift.
It is a popular stochastic method for simulating stock prices that follow a trend while experiencing a random walk of up-and-downs characterizing risk.

The following notes were used for my implementation of GBM:

http://www.columbia.edu/~ks20/FE-Notes/4700-07-Notes-BM.pdf

http://www.columbia.edu/~ks20/FE-Notes/4700-07-Notes-GBM.pdf

**GBM Simulation Results on SPY (S&P 500; Jun 9, 2023)**

![alt text](https://github.com/junyoung-sim/gbm/blob/main/res/gbm_sample_path.png)

![alt text](https://github.com/junyoung-sim/gbm/blob/main/res/gbm_lognormal_prices.png)

**Short-Term Valuation Cycle**

Using the simulation shown above, we can estimate the probability that the asset value would be greater than the current value during the N-day period following the current time.

At every time ***t***, observe the asset value's historical data during the past 6-months (120 days). Through the GBM simulation, estimate the probability that the asset value would be greater than the current value during the 100-day period following ***t***. This probability is impacted by the short-term mean return and variation in return (or volatility and risk) according to the principles of GBM.

Repeat the same procedure for every ***t*** and we get the following output.

![alt text](https://github.com/junyoung-sim/gbm/blob/main/res/gbm-short-term-valuation-cycle.png)

The graph on the top shows the probabilities estimated through the simulation each day for the S&P 500. Notice that those probabilities appear to be leading indicators; once the probabilities reach a significant value (below 0.30 and above 0.80), the stock index reverses direction!