Identity Validation API (Aadhaar & PAN) — FastAPI + Pytest  
A clean and modular Identity Validation Microservice built using FastAPI.
This project validates Aadhaar and PAN numbers and includes a complete automated test suite using pytest.
It also demonstrates a reusable fraud scoring module and a scalable backend architecture suitable for QA automation or backend development learning.  

🚀 Features  
✅ Aadhaar Validation

Validates Aadhaar number format

Tested with positive and negative inputs

Modular utility function  

✅ PAN Validation

Validates PAN format using regex

Includes extensive unit tests

Follows Indian PAN format rules  

✅ Fraud Detection Logic

A simple rule-based engine:

Invalid Aadhaar → +50

Invalid PAN → +50

Fraud if score ≥ 50  

Located in:
app/helpers/fraud_detection.py  

✅ Automated Test Suite (Pytest)

--Tests include:

Aadhaar validation

PAN validation

Fixtures via conftest.py

Utility helpers for test reusability  

📁 Project Structure  
app/
  helpers/
    fraud_detection.py        # Fraud scoring module  
  templates/
    dashboard.html            # Template placeholder  
  database.py                 # (optional) DB integration structure  
  main.py                     # FastAPI application entry point  

tests/
  api/
    test_aadhaar_validation.py
    test_pan_validation.py
  config/  
    settings.py               # Config for test environment   
  utils/  
    helpers.py                 # Shared test utilities    
  conftest.py                   # Global pytest fixtures  

README.md  
requirements.txt  

▶️ Run the Server  
Install dependencies:  
pip install -r requirements.txt  

Run API:  
uvicorn app.main:app --reload  

Open APIs at:  
http://localhost:8000/docs  

🧪 Run Tests  
pytest -v  

💡 Why This Project Is Useful  
This microservice is ideal for:

1. QA Automation Engineers (API testing + pytest experience)

2. Backend Developers learning FastAPI

3. FinTech-style validation workflows

4. Fraud detection rule engine demonstrations

5. Modular Python project structure showcase

📌 Future Enhancements  
1. Add a Combined KYC API

2. Store validated records in a database

3. Build fraud analytics dashboard

4. Add authentication (API Key / JWT)

5. CI/CD with GitHub Actions

6. Docker support

👨‍💻 Author

Hrishabh Pal  
Python Learner | QA Automation Aspirant