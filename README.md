🛡️ KYC Fraud Detection System
PAN & Aadhaar Validator — FastAPI + MongoDB + Jinja2 Dashboard

This project is a simple yet practical KYC Fraud Detection System where users can validate PAN and Aadhaar numbers.
Each validation request is logged into MongoDB, and a web dashboard shows live statistics.

This is a great beginner-friendly backend project built using FastAPI + MongoDB Atlas.

🚀 Features

✔ PAN Validation using Regex
✔ Aadhaar Validation using Verhoeff algorithm
✔ MongoDB Logging for every request
✔ Jinja2 HTML Dashboard to view stats
✔ Clean API documentation using Swagger UI

🛠️ Tech Stack

| Layer             | Technology    |
| ----------------- | ------------- |
| Backend Framework | FastAPI       |
| Database          | MongoDB Atlas |
| Template Engine   | Jinja2        |
| Web Server        | Uvicorn       |
| Language          | Python        |

📁 Project Structure

kyc-fraud-detection/
│── app/
│    ├── main.py                # FastAPI app + routes
│    ├── database.py            # MongoDB setup
│    └── templates/
│         └── dashboard.html    # Stats dashboard
│
│── .env                        # Mongo connection URL
│── requirements.txt
│── .gitignore
│── README.md

▶️ Installation & Setup  
️1. Install dependencies  
pip install -r requirements.txt  
2️. Add MongoDB URL  
MONGO_URL="your-mongodb-url"  
3️. Run the server  
uvicorn app.main:app --reload  


🌐 API Endpoints  
Health Check  
GET /health  

Validate PAN  
GET /validate-pan?pan=ABCDE1234F  

Validate Aadhaar  
GET /validate-aadhaar?aadhaar=987654321012  

Dashboard  
GET /dashboard  

📊 Dashboard Preview  
Shows:  
Total API calls  
Valid / invalid PAN
Valid / invalid Aadhaar  
Rendered using Jinja2 Templates.  

🔒 Environment Variables  
|`MONGO_URL` | MongoDB Atlas connection string |

👨‍💻 Author

Hrishabh Pal  
Python Learner | QA Automation Aspirant