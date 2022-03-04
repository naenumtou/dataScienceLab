# ✍🏻 The data science lab

![Google Colab](https://img.shields.io/badge/Editor-Google%20Colab-brightgreen)
![VS Code](https://img.shields.io/badge/Editor-VS%20Code-brightgreen)
![SAS](https://img.shields.io/badge/Editor-SAS-brightgreen)
![Python](https://img.shields.io/badge/Code-Python-blue)
![SAS](https://img.shields.io/badge/Code-SAS-blue)
![pickle](https://img.shields.io/badge/Tools-pickle-brightgreen)

<p align="center">
  <img src="https://research.phoenix.edu/sites/default/files/blogpost/images/statistical-analysis-hero.jpg" alt="The statistical models"/>
</p>

The repository is contained the several models as well as models tutorial. There are various kinds of works related such as:
* Time series model: It covers statistical analytics on time series data.
* Statistic analysis / technique: This provides useful / helpful statistical tasks that could be integrate in the models.
* Libraries tutorial: The useful python libraries provides as the tutorials, which is effortless to follow.
* Deployment: The branch to keep materials for ML Model deployment.
* Computer vision: It contained both of notebook file and branch realted to computer vision topic.
* Market risk: This is not my main area, which is credit risk. Thus, all related to market risks are placed under this topic.
* Customer and Marketing: Recently, it is better to know how to apply data science skills with marketing areas.
* PySpark: 
* Natural language processing (NLP): 
* Others: 

There will be many more to come in the future.

## Time series model
* `bayesian_linear_regression.ipynb`: The Bayesian linear regression is an approach to linear regression in which the statistical analysis is undertaken within the context of Bayesian inference.
* `ARIMAModel.ipynb`: The ARIMA Model (Autoregressive Integrated Moving Average) used for stock price prediction.
* `SARIMAModel.ipynb`: The SARIMA Model (Seasonal Autoregressive Integrated Moving Average) used for oil price prediction.
* `pca.ipynb`: The Principal Component Analysis (PCA) appiled for time series data.
* `pcr.ipynb`: The Principal Component Analysis (PCA) with linear regression appiled for time series data.
* `pls_regression.ipynb`: The Partial Least Squares (PLS) for time series data.
* `timeSeriesSlide.ipynb`: The time series model cross validation with time slide window.
* `timeSeriesSplit.ipynb`: The time series model cross validation with time split window.
* `timeSplit.sas`: Utilised SAS to perform the time series model cross validation with time split window.

## Statistic analysis / technique
* `MICE.ipynb`: MICE is the Multivariate Imputation by Chained Equations.
* `SHAPInterpreter.ipynb`: SHAP values are used to explain individual predictions made by a model.
* `chi_squareTest.ipynb`: The Chi-square test for categorical data.
* `k-fold.sas`: Utilised SAS to perform K-Fold cross validation.
* `one_hot_encoding.ipynb`: The transformation categorical data for modelling purpose.

## Libraries tutorial
* `PyCaretModel.ipynb`: PyCaret is an open source, low-code machine learning library.
* `optimumBinning.ipynb`: The tutorial for using OptBinning library to develop credit score card.
* `pipelineModel.ipynb`: The tutorial for using Pipiline module in scikit-learn library.

## Deployment
* `localHostDeploy`: The ML Model local host deployment using `Flask`.
* `dockerDeploy`: The ML Model local host deployment using docker.

## Computer vision
* `KimJoug_unModel.ipynb`: The face recognition model of Kim Jong-un with `dlib` library.
* `LisaFaces.ipynb`: The face recognition model with a few lines of code using `face_recognition` library.
* `agePrediction.ipynb`: The age prediction from image using `age_net.caffemodel` pre-trained model.
* `face_recognition_pca_svm.ipynb`: Building face recognition by using Principal Component Analysis (PCA) and Support Vector Machine (SVM).
* `HOGClassification.ipynb`: Building car logo classification model by using histogram of oriented gradients (HOG) with K-Nearest neighbor.
* `slidingWindow.ipynb`: Sliding window for image processing.
* `nonMaximumSuppression.ipynb`: Non-maximum suppression for true positive image processing.
* `classicObjectDetection.ipynb`: Apply HOG Features extraction with image sliding window and Non-maximum suppression to create object detection model.
* `faceTracking.ipynb`: Object tracking using FaceNet model for face detection. Then, using OpenCV as the tracker.
* `faceMaskTiny`: The face maks detection using YOLOV4-Tiny pre-trained model from Darknet.

## Market risk
* `sharpeRatio.ipynb`: Portfolio optimisation using Sharpe ratio.

## Customer and Marketing
* `RFMAnalysis.ipynb`: The customer segmentation with RFM Analysis.
* `marketBasket.ipynb`: The market basket analysis to uncover associations between items in the shop.

## Natural language processing (NLP)
* `reExample.py`: The regular expression (RegEx) by python. To deal with text mining for NLP.
* `twitterIO.ipynb`: The TwitterIO data analytics to find inside topic of fake accounts by Information Operation (IO).
* `twitterIOLSA.ipynb`: The topic modelling of TwitterIO Dataset using LSA Model.

## PySpark
* `PySparkUsedcarData.ipynb`: The basic data processing using PySpark library.

## Others
* `COVIDLogScale.ipynb`: The plot of log-scale for COVID-19 Stop pandemic.
* `ExcelWorkingfile.ipynb`: The integration of python and Excel using `XlsxWriter`.
* `RVModelRandomForest.ipynb`: The used car residual values model using Random Forest Regression with Double Declining Balance (DDB) function.
* `sir_seir_model.ipynb`: The simulation model for COVID-19 pandemic.
* `googleScraping.ipynb`: The web-scraping by `BeautifulSoup`.
* `interview.py`: The question during interview process.
