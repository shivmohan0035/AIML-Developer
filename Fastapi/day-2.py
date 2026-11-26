from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# using Pydantic models to define the request body for the loan application
# pydantic is a data validation and settings management library that uses Python type annotations
class LoanApplication(BaseModel):
    name: str
    age: int
    income: float
    loan_amount: float
    credit_score: int
    
@app.post("/predict")
def predict_loan(loan: LoanApplication):
    if loan.age < 18  or loan.age > 65 or loan.income < 20000 or loan.credit_score < 600:
        decision = "Rejected"
    else:
        decision = "Approved"
    
    return {
        "name": loan.name,
        "age": loan.age,
        "income": loan.income,
        "loan_amount": loan.loan_amount,
        "credit_score": loan.credit_score,
        "decision": decision
    }