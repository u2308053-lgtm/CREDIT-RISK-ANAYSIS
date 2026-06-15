# CREDIT-RISK-ANAYSIS
A machine learning model that uses decision tree classifier to classify if a person can repay his/her loan based on the amount of money being borrowed

## Parameters Used

- Monthly income
- Employment type
- Years of experience
- Existing EMI
- Monthly expenses
- Credit score
- Number of previous defaults
- Number of past loans
- Late payment count
- Total loan amount
- Loan tenure (months)
- Loan type
- DTI ratio
- Relationship years
- Existing customer status

## Pipeline

1. Input Customer ID

2. Check whether the ID exists:

### If ID exists:
- Load customer details
- Train Decision Tree Classification model
- Predict repayment risk
- Display risk result

### If ID does not exist:
- Ask user whether they want to register

If yes:
- Collect customer details
- Add customer information to dataset
- Store updated dataset

If no:
- Ask for ID again

## Algorithm Used

- Decision Tree Classifier

## Output

The model classifies customers into:

- Low Risk
- High Risk

## Technologies Used

- Python
- Pandas
- Scikit-learn
