# Email-Spam-Detector-Python-Sklearn
This is a ML (Machine Learning) model created using Sklearn, this model Detects of the email is Ham/Not Spam [0], Phishing [1], and Spam [2]. The model is trained on 292,360 rows and tested on 73,090 rows, where it reached a high accuracy of 95%.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)


**Dataset** Used:
```
https://www.kaggle.com/datasets/akshatsharma2/the-biggest-spam-ham-phish-email-dataset-300000?hl=en-IN
```

# How the **Model** Works
The model is tested and we'll trained, the model outputs 3 possibilities:

```
Spam [2]
Phishing [1]
Ham/Not Spam [0]
```

# **Libraries** used in the project

1. sklearn 1.9.0 (Scikit-learn)
2. pandas 3.0.5
3. numpy 2.4.4
4. joblib 1.5.3
5. python 3.14.6 (This is a language)

![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)

![Joblib](https://img.shields.io/badge/Joblib-FF6F00?style=for-the-badge&logo=python&logoColor=white)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

 NOTE:- You only need **joblib** and **python** for loading the model, since rest were for training and Testing purpose, which is already done.

# **Classification Report** and **Confusion Matrix**
```
---- Classification Report ----
              precision    recall  f1-score   support

           0       0.99      0.98      0.98     33705
           1       0.93      0.74      0.83      8627
           2       0.91      0.97      0.94     30758

    accuracy                           0.95     73090
   macro avg       0.95      0.90      0.92     73090
weighted avg       0.95      0.95      0.95     73090

---- Confusion Matrix ----
[[33087     4   614]
 [   23  6420  2184]
 [  392   448 29918]]
```
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
