# 🚀 B2B Lead Intelligence Pipeline

## 📌 Problem Statement

Businesses such as marketing agencies, SaaS companies, and consulting firms require **high-quality leads of potential clients**. However, relevant company data is scattered across multiple platforms and is often unstructured, incomplete, and inconsistent.

Manual data collection is time-consuming and not scalable, while existing paid tools are expensive and inaccessible for small businesses.

---

## 🎯 Solution

This project builds an **automated data engineering pipeline** that:

* Scrapes startup/company data from Y Combinator
* Cleans and standardizes the raw data
* Stores structured data in a MongoDB database
* Automatically updates data at regular intervals
* Provides a dynamic interface using Streamlit for business users

---

## 🏗️ Architecture

```
Scraper → Raw Data → Cleaning → MongoDB → Streamlit Dashboard
```

---

## ⚙️ Tech Stack

* **Python** – Core programming language
* **BeautifulSoup / Requests** – Web scraping
* **Pandas** – Data cleaning and transformation
* **MongoDB** – Database for storing structured data
* **Streamlit** – Interactive dashboard
* **APScheduler** – Automation of pipeline

---

## 🔍 Features

* ✅ Automated web scraping with error handling
* ✅ Data cleaning and standardization
* ✅ MongoDB integration for storage
* ✅ Scheduled pipeline execution (every 12 hours)
* ✅ Interactive dashboard with:

  * Search functionality
  * Data visualization
  * Real-time data display

---

## 📂 Project Structure

```
b2b-lead-pipeline/
│
├── scraper/
│   └── yc_scraper.py
│
├── processing/
│   └── clean_data.py
│
├── database/
│   └── db.py
│
├── app/
│   └── streamlit_app.py
│
├── scheduler/
│   └── scheduler.py
│
├── data/
│   ├── raw.json
│   └── cleaned.json
│
├── requirements.txt
├── README.md
└── .env
```

---

## 🚀 How to Run Locally

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/b2b-lead-pipeline.git
cd b2b-lead-pipeline
```

---

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Start MongoDB

Make sure MongoDB is running locally:

```
mongodb://localhost:27017/
```

---

### 4️⃣ Run the pipeline manually

```
python scraper/yc_scraper.py
python processing/clean_data.py
python database/db.py
```

---

### 5️⃣ Run Streamlit dashboard

```
streamlit run app/streamlit_app.py
```

---

### 6️⃣ Run scheduler (optional)

```
python scheduler/scheduler.py
```

---

## 🔐 Environment Variables

Create a `.env` file:

```
MONGO_URI=mongodb://localhost:27017/
DB_NAME=b2b_db
```

---

## 📊 Output

The system provides:

* Clean, structured company data
* Searchable dashboard
* Automatically updated dataset

---

## 💼 Business Value

This solution enables businesses to:

* Discover potential clients (lead generation)
* Filter companies by relevance
* Access clean and structured data
* Reduce dependency on expensive third-party tools

---

## 🤖 Future Enhancements (Optional)

* Lead scoring using machine learning
* Industry classification using NLP
* Email/contact extraction
* API deployment for external access

---

## 🧠 Key Learnings

* Building end-to-end data pipelines
* Handling unstructured web data
* Automating workflows
* Designing systems for real-world business use cases

---

## 📌 Author

**Sanket Khapake**
Aspiring Data Engineer | MERN Stack Developer | Data Science Enthusiast

---
