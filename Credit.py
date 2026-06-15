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

while True:
    
    a = int(input("Enter id: "))

    if a in df["customer_id"].values:

        b = input(f"Hi {a}, welcome back. Would you like me to check if you can repay your loan on time? ")

        if b=="yes":

            c = int(input("Enter how much money you need to borrow: "))
            df.loc[df["customer_id"] == a, "loan_amount"] = c
            print(probability(a))

        else:
            print("No problem,have a nice day.")
            exit()

    if a not in df["customer_id"].values:
        c=input("Welcome, is this a new id");

        if c=="yes":
            d=input("Would you like me to register it in the system?")

            if d=="yes":

                Input1 = input("existing customer: ")
                
                Input2 = input("relationship years: ")

                Input3 = float(input("monthly income: "))
                
                Input4 = input("employment type: ")
                
                Input5 = float(input("experience: "))
                
                Input6 = float(input("existing emi: "))
                
                Input7 = float(input("monthly expenses: "))
                
                Input8 = float(input("credit score: "))
                
                Input9 = int(input("number of previous defaults: "))
                
                Input10 = int(input("number of past loans: "))
                
                Input11 = int(input("late payments count: "))
                
                Input12 = float(input("previous loan amount: "))
                
                Input13 = int(input("loan tenure months: "))
                
                Input14 = input("loan type: ")
                
                Input15 = float(input("dti ratio: "))

                new_customer = {
                "customer_id": a,
                "is_existing_customer": Input1,
                "relationship_years": Input2,
                "monthly_income": Input3,
                "employment_type": Input4,
                "years_in_job": Input5,
                "existing_emi": Input6,
                "monthly_expenses": Input7,
                "credit_score": Input8,
                "previous_default": Input9,
                "number_of_past_loans": Input10,
                "late_payments_count": Input11,
                "loan_amount": Input12,
                "loan_tenure_months": Input13,
                "loan_type": Input14,
                "dti_ratio": Input15
                }
            
                df.loc[len(df)] = new_customer

                df.to_csv("Credit_dataset.csv", index=False)

            else:
                print("Okey,have a nice day")

        else:
            print("Okey,enter again")
            
        
                
                            
                                
                                

                

            

            
