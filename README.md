# Python ARMA(p,q) Model Fitter

The purpose of this notebook is to get accustomed to the time series modeling capabilities of python, and it's associated libraries.

## Data Generator Scripts

The (currently 2) provided scripts generate data for AR(2) and ARMA(2,3) processes. The domain of these series cover January 1st of 2022 until April 10th 2022, which is exactly 100 days.
In the notebook for the model generating there are plots for both series, as well as plots for the ACF/PACF for both series.

## Modeling Notebook

The modeling part of this notebook uses the statsmodels package. This includes a built in ARMA function, with parameters for p/d/q. With p being the order of the AR coefficients, d being the differencing to make the process stationary, and q being the order of the MA coefficient.
