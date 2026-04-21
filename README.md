# 📊 Basic AI News Dashboard

A real-time news aggregation and analysis platform. This project uses FastAPI to serve an AI-powered prediction model and Streamlit to provide a clean, interactive user dashboard.

## 🚀 Live Demo

* **Dashboard:** https://waflpredic.streamlit.app/
* **API Documentation:** https://news-dashboard-s7q8.onrender.com/docs

---

## 🛠️ Technology Stack

* **Frontend:** [Streamlit](https://streamlit.io) for the interactive dashboard.
* **Backend API:** [FastAPI](https://tiangolo.com) for serving predictions.
* **Deployment:** [Render](https://render.com) (Backend) & [Streamlit Community Cloud](https://streamlit.io) (Frontend).
* **AI/ML:** Custom prediction model served via FastAPI.
* **Data Source:** News data via: https://newsdata.io

---

## 📁 Project Structure

```text
├── SRC/
│   ├── api.py          # FastAPI application (Backend)
│   ├── app.py          # Streamlit application (Frontend)
│   ├── fetch.py        # News fetching & cleaning logic
│   └── train.py        # AI Training & Testing
├── requirements.txt    # Project dependencies
└── README.md
```

---

## ⚙️ Installation & Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/wafiai/News-Dashboard
cd News-Dashboard
```

### 2. Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Environment Variables
Create a `.env` file in the root directory and add your keys:
```text
NEWS_API_KEY = "your_key_here"
RENDER_API_URL = "https://news-dashboard-s7q8.onrender.com/predict"
```

### 4. Run the project
* **Start API:** `uvicorn SRC.api:app --reload`
* **Start Dashboard:** `streamlit run SRC.app.py`

---

## 🔐 Deployment Notes

* **Secrets Management:** API keys are managed via Streamlit Secrets and Render Environment Variables to ensure security.
* **Cold Starts:** The backend API on Render (free tier) may take ~30 seconds to wake up on the first request.
