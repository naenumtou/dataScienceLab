# ✍🏻 The statistical models

![Google Colab](https://img.shields.io/badge/Editor-Google%20Colab-brightgreen)
![VS Code](https://img.shields.io/badge/Editor-VS%20Code-brightgreen)
![SAS](https://img.shields.io/badge/Editor-SAS-brightgreen)
![Python](https://img.shields.io/badge/Code-Python-blue)
![SAS](https://img.shields.io/badge/Code-SAS-blue)

<p align="center">
  <img src="https://research.phoenix.edu/sites/default/files/blogpost/images/statistical-analysis-hero.jpg" alt="The statistical models"/>
</p>

The statistical models repository is contained the model or analysis, which are not apart of IFRS 9 or Credit Risk. There are various kinds of statistical model / techniques, which may helpful to adapt other general cases.

## Time series model
* `bayesian_linear_regression.ipynb`: The Bayesian linear regression is an approach to linear regression in which the statistical analysis is undertaken within the context of Bayesian inference
* `ARIMAModel.ipynb`: The ARIMA Model (Autoregressive Integrated Moving Average) used for stock price prediction
* `SARIMAModel.ipynb`: The SARIMA Model (Seasonal Autoregressive Integrated Moving Average) used for oil price prediction
* `pca.ipynb`: The Principal Component Analysis (PCA) appiled for time series data
* `pcr.ipynb`: The Principal Component Analysis (PCA) with linear regression appiled for time series data
* `pls_regression.ipynb`: The Partial Least Squares (PLS) for time series data
* `timeSeriesSlide.ipynb`: The time series model cross validation with time slide window
* `timeSeriesSplit.ipynb`: The time series model cross validation with time split window
* `timeSplit.sas`: Utilised SAS to perform the time series model cross validation with time split window

## Statistic analysis / technique
* `MICE.ipynb`: MICE is the Multivariate Imputation by Chained Equations
* `SHAPInterpreter.ipynb`: SHAP values are used to explain individual predictions made by a model
* `chi_squareTest.ipynb`: The Chi-square test for categorical data
* `k-fold.sas`: Utilised SAS to perform K-Fold cross validation
* `one_hot_encoding.ipynb`: The transformation categorical data for modelling purpose

## Libraries tutorial
* `PyCaretModel.ipynb`: PyCaret is an open source, low-code machine learning library
* `optimumBinning.ipynb`: The tutorial for using OptBinning library to develop credit score card
* `pipelineModel.ipynb`: The tutorial for using Pipiline module in scikit-learn library

## Computer vision
* `LisaFaces.ipynb`: The face recognition model with a few lines of code using `face_recognition` library
* `face_recognition_pca_svm.ipynb`: Building face recognition by using Principal Component Analysis (PCA) and Support Vector Machine (SVM)
* `HOGClassification.ipynb`: Building car logo classification model by using histogram of oriented gradients (HOG) with K-Nearest neighbor
* `slidingWindow.ipynb`: Sliding window for image processing
* `nonMaximumSuppression.ipynb`: Non-maximum suppression for true positive image processing
* `classicObjectDetection.ipynb`: Apply HOG Features extraction with image sliding window and Non-maximum suppression to create object detection model

## Market risk
* `sharpeRatio.ipynb`: Portfolio optimisation using Sharpe ratio

## Customer and Marketing
* `RFMAnalysis.ipynb`: The customer segmentation with RFM Analysis

## Natural language processing (NLP)
* `twitterIOLSA.ipynb`: The topic modelling of TwitterIO Dataset using LSA Model

## Model (Others)
* `sir_seir_model.ipynb`: The simulation model for COVID-19 pandemic
