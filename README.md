# Email-Spam-Detector-Python-Sklearn
This is a ML (Machine Learning) model created using Sklearn, this model Detects of the email is Ham/Not Spam [0], Phishing [1], and Spam [2]. The model is trained on 292,360 rows and tested on 73,090 rows, where it reached a high accuracy of 95%.

**,sa  Dataset** Used:
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
1. numpy
2. pandas
3. sklearn
4. joblib

 NOTE:- You only need **joblib** for loading the model, since rest were for training and Testing purpose, which is already done.

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
