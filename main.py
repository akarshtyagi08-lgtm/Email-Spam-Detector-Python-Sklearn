# Import Joblib for loading Model
import joblib

# Import Model and Tokenizer
model = joblib.load("Email_Spam_Detector.joblib")
tokenizer = joblib.load("Tokenizer.joblib")

# Take email and tokenize it for model
email = input("Enter Email: ")
tokenized_email = tokenizer.transform([email])

# Get Prediction
prediction = model.predict(tokenized_email)

# Print the result
if prediction == 2: # 2 means Spam
    print(" Result: Spam [2]")
elif prediction == 1: # 1 means Phishing
    print("Result: Phishing [1]")
else: # 0 means Ham/Not Spam
    print("Result: Ham/Not Spam [0]")