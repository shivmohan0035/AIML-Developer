# path parameter {} ---> It allows you to define dynamic segments in your API endpoints, enabling you to create more flexible and interactive routes.

#  /customer/101

from fastapi import FastAPI

app = FastAPI()

@app.get("/customer/{item_id}")
def get_customer(item_id: int):
    return {"item_id": item_id, "message": f"Customer details for item_id {item_id}"}
  
# query parameter ? ---> It allows you to pass additional information to your API endpoints in the form of key-value pairs, enabling you to filter, sort, or customize the response based on specific criteria.

# /customer?name=John&age=30
@app.get("/customer")
def get_customer_details(name: str = None, age: int = None):
    if name and age:
        return {"message": f"Customer details for {name}, age {age}"}
    elif name:
        return {"message": f"Customer details for {name}"}
    elif age:
        return {"message": f"Customer details for age {age}"}
    else:
        return {"message": "No customer details provided."}