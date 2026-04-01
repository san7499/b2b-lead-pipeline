# 🚀 B2B Lead Intelligence Pipeline

## 📌 Problem Statement

Businesses such as marketing agencies, SaaS companies, and consulting firms require **structured data** to identify potential clients and make data-driven decisions. However, most available data online is:

* Unstructured
* Inconsistent
* Scattered across multiple sources

Manual data collection is time-consuming and inefficient.

---

## 🎯 Solution

This project implements an **end-to-end data engineering pipeline** that:

* Scrapes publicly available data from a website
* Cleans and standardizes the data
* Stores it in a MongoDB database
* Displays it through an interactive Streamlit dashboard

---

## 🏗️ Architecture

```
Scraper → Raw Data → Data Cleaning → MongoDB → Streamlit Dashboard
```

---

## ⚙️ Tech Stack

* **Python** – Core language
* **Requests + BeautifulSoup** – Web scraping
* **Pandas** – Data handling
* **MongoDB** – Database
* **Streamlit** – Interactive UI
* **APScheduler** – Automation

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
```

---

## 🔍 Features

* ✅ Automated data scraping
* ✅ Data cleaning and preprocessing
* ✅ MongoDB integration
* ✅ Interactive Streamlit dashboard
* ✅ Search functionality
* ✅ Modular pipeline design
* ✅ Error handling and logging

---

## 🚀 How to Run the Project

### 1️⃣ Clone the repository

```
git clone https://github.com/san7499/b2b-lead-pipeline.git
cd b2b-lead-pipeline
```

---

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Ensure MongoDB is running

```
mongodb://localhost:27017/
```

---

### 4️⃣ Run the pipeline

```
python scraper/yc_scraper.py
python processing/clean_data.py
python database/db.py
```

---

### 5️⃣ Run the dashboard

```
streamlit run app/streamlit_app.py
```

---

## 🔐 Environment Variables (Optional)

You can use a `.env` file:

```
MONGO_URI=mongodb://localhost:27017/
DB_NAME=b2b_db
```

---

## 📊 Output

* Cleaned structured dataset stored in MongoDB
* Interactive dashboard to explore data
* Search-based filtering

---

## 💼 Business Value

This solution enables businesses to:

* Discover structured datasets
* Quickly search and analyze information
* Reduce manual data collection effort
* Build scalable data pipelines

---

## ⚠️ Note

Initially, the project attempted to scrape dynamic websites, which led to unreliable data extraction. To ensure stability and consistency, a structured and static dataset was used for building a reliable pipeline.

---

## 🧠 Key Learnings

* Building end-to-end ETL pipelines
* Handling unstructured web data
* Data cleaning and validation
* Database integration
* Creating interactive dashboards

---

## 🤖 Future Enhancements

* Add data visualization charts
* Integrate machine learning for insights
* Deploy API endpoints
* Use cloud database (MongoDB Atlas)
* Improve scraping with dynamic handling

---

## 👨‍💻 Author

**Sanket Khapake**
Aspiring Data Engineer | Full Stack Developer | Data Science Enthusiast

---
