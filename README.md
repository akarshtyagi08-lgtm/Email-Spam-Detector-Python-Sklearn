# Email-Spam-Detector-Python-Sklearn
This is a ML (Machine Learning) model created using Sklearn, this model Detects of the email is Ham/Not Spam [0], Phishing [1], and Spam [2]. The model is trained on 292,360 rows and tested on 73,090 rows, where it reached a high accuracy of 95%.

Dataset Used:
```
https://www.kaggle.com/datasets/akshatsharma2/the-biggest-spam-ham-phish-email-dataset-300000?hl=en-IN
```

# How the Model Works
The model is tested and we'll trained, the model outputs 3 possibilities:

```
Spam [2]
Phishing [1]
Ham/Not Spam [0]
```

# Libraries used in the project
1. numpy
2. pandas
3. sklearn
4. joblib

 NOTE:- You only need **joblib** for loading the model, since rest were for training and Testing purpose, which is already done.
