# NASA NEO Hazardous Asteroid Prediction using K-Nearest Neighbors (KNN)

Heroku:
https://elijahcw-final-75b3048251ed.herokuapp.com/
![image](https://github.com/elijahcw-git/NEO_threat_prediction/assets/85442180/d31b585d-4c9d-46db-997d-fab909870cf3)

## Overview

This project is developed to predict whether Near-Earth Objects (NEOs) in the NASA NEO dataset are hazardous or not using the K-Nearest Neighbors (KNN) algorithm. The objective is to achieve a model accuracy of 93% by selecting specific features from the dataset that are most relevant for the prediction.

## Dataset

The dataset used for this prediction project is the NASA NEO (Near-Earth Object) dataset. It contains information about NEOs, including their estimated diameter, relative velocity, miss distance, and absolute magnitude.

## Features Used for Prediction

The model uses the following features from the NASA NEO dataset:

- Estimated Minimum Diameter (`est_diameter_min`)
- Estimated Maximum Diameter (`est_diameter_max`)
- Relative Velocity (`relative_velocity`)
- Miss Distance (`miss_distance`)
- Absolute Magnitude (`absolute_magnitude`)

## Tools and Libraries

The model is developed using Python and makes use of the following libraries:

- scikit-learn (`sklearn`): For implementing the K-Nearest Neighbors (KNN) algorithm.
- pandas: For data manipulation and analysis.

## Model Training

The KNN model is trained on the NASA NEO dataset using `scikit-learn`. The dataset is processed, and the features are carefully chosen to ensure that the most relevant predictors are used for the model.

## Model Evaluation

The performance of the model is assessed based on its accuracy in predicting whether NEOs are hazardous or not. The target is to achieve a model accuracy of 93%.

---

This README provides an overview of the NASA NEO Hazardous Asteroid Prediction project using K-Nearest Neighbors (KNN). For more details and code implementation, refer to the associated Python notebook.
