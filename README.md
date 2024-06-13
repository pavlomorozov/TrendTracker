# TrendTracker
This Python script demonstrates how to identify trends in time series data using linear regression. It calculates correlation coefficient to determine whether the data shows an upward trend, downward trend, or no trend.

In our scenario, input values for linear regression will be:

- x: time interval number [0,1,2,…,n]
- y: value at a particular interval [V0,V1,V2,…,Vn]

The correlation coefficient R is a value in the range [−1,1] and it is higher when the values in the datasets fit better. In our case, the list x, containing time interval data, is perfectly linear. Thus, a correlation coefficient R of 1 would indicate a perfect linear trend in our y dataset! If we would get a correlation coefficient R of -1, it would indicate a perfectly linear downward trend.

Researchers can define their own interval of correlation coefficient R values to determine if a trend is strong enough for their purpose. For example, R:

- [0.7, 1] Strong linear upward trend
- (−0.7, 0.7) Trend is weak or no trend identified
- [−1, −0.7] Strong linear downward trend

See more on [How to Identify Trending Time Series (Linear Regression)](https://medium.com/@pavlomorozov78/how-to-identify-trending-time-series-dda0f68a47fa)
