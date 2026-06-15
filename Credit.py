import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("Credit_dataset.csv")

def probability(a):

    X = df[["is_existing_customer","relationship_years","monthly_income","employment_type",
            "years_in_job","existing_emi","monthly_expenses","credit_score",
            "previous_default","number_of_past_loans","late_payments_count",
            "loan_amount","loan_tenure_months","loan_type","dti_ratio"]]

    Y = df["loan_result"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=42)
    model = DecisionTreeClassifier()
    model.fit(X_train, Y_train)
    customer = df[df["customer_id"] == a]
    result = model.predict(customer[X.columns])
    return result


a = int(input("Enter id: "))

if a in df["customer_id"].values:

    b = input(f"Hi {a}, welcome back. Would you like me to check if you can repay your loan on time? ")

    if b=="yes":

        c = int(input("Enter how much money you need to borrow: "))
        df.loc[df["customer_id"] == a, "loan_amount"] = c
        print(probability(a))