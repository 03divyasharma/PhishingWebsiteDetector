# Phishing Website Detection
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)   ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)        ![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)     ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)


![Model](https://cloud.google.com/static/architecture/images/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning-1-elements-of-ml.png)

## About
This project is developed as part of the iNeuron.ai internship. The primary objective of this project is to build  a model using  Machine Learning  which can accurately predict whether a website is phishing or safe. 

## Description
Phishing is an attempt of fraudulently accessing sensitive or confidential information of an internet user by appearing as a trusted person or entity. It is a social engineering attack that aims at exploiting the weakness found in system processes as caused by system users.
 
## Features
- Website URL analysis for phishing indicators.
- Machine learning model integration for accurate phishing detection.
- Web interface for easy interaction (Entering features manually gives an accuracy of __96.2%__)


## Data Description
https://data.mendeley.com/datasets/72ptz43s9v/1


## Technologies Used
### Database used: 

 MySQL 





### Machine Learning Libraries
![image](https://github.com/03divyasharma/Phishing-Website-Detector/assets/155889534/6a1ab305-e8bb-465b-ac9e-9383b30d4669)                     ![image-6](https://github.com/03divyasharma/Phishing-Website-Detector/assets/155889534/ec2f63ef-77a1-46cd-a3d1-2bf963a11d1c)
                                          ![image-7](https://github.com/03divyasharma/Phishing-Website-Detector/assets/155889534/c401b5d0-1e52-448f-a071-2e3890eeb36b)



For Feature Selection : Yellowbrick by Scikit Learn 

![image-8](https://github.com/03divyasharma/Phishing-Website-Detector/assets/155889534/6e4a3440-d0ec-4411-ae94-6d2b6a844d75)




### IDE: 
For building Random Forest Classifier model

![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)

For end-to-end project

![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

## Deployment :
![image-10](https://github.com/03divyasharma/Phishing-Website-Detector/assets/155889534/e18d19a8-33f0-4d21-b41e-2f2579d83217)    

![image-12](https://github.com/03divyasharma/Phishing-Website-Detector/assets/155889534/bef54126-90d0-4362-ab74-bee1fc566954)

 This ML feature is deployed by creating a Flask frontend and as static web app using Azure. 



## [Random Forest Classifier](https://machinelearningmastery.com/random-forest-ensemble-in-python/): 
The model achieved after hyperparameter tuning had following parameters:

RandomForestClassifier(max_depth=20, min_samples_leaf=2, min_samples_split=13,
n_estimators=105)

## Accuracy Achieved

 Classification Report using Yellowbrick 

![image-11](https://github.com/03divyasharma/Phishing-Website-Detector/assets/155889534/e8d600fe-df02-4797-953a-a022127f0a86)

```


## Initialize the Git Repositry
``` git init

git add .
    
git commit -m "Initial commit"
    
git branch -M main
    
git remote add origin <github_url>
    
git push -u origin main
```
    
 ## To modify on github 
  ```git add .
  
   git commit -m "proper message"
   
   git push -u origin main
```


## External Links

[Azure Static Web Apps](https://learn.microsoft.com/en-us/azure/static-web-apps/)

