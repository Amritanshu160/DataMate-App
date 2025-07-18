# 📊 DataMate – Your All-in-One AI Data Assistant 💡

**DataMate** is a powerful, interactive data science assistant that enables users to analyze, visualize, model, and chat with datasets — all in one unified AI-powered platform.

> ⚡ Built for data scientists, analysts, students, and enthusiasts who want to explore and model data quickly without writing extensive code.

---

## 🚀 Features

### 🧠 AI-Powered Interactions
- **💬 Chat with CSV**: Ask questions and get insights from your uploaded CSV files in natural language.

### 🧮 SQL & Data Intelligence
- **🧾 Text to SQL Generator**: Convert natural language questions into SQL queries to run on uploaded datasets automatically.

### 📈 Visualization Tools
- **📊 Plotly Data Visualizer**: Instantly generate interactive charts (bar, scatter, line, pie, etc.) on any uploaded dataset using Plotly.
- **📋 Exploratory Data Analysis (EDA)**: Automatically perform EDA and generate statistical summaries, null value reports, correlation matrices, outlier detection, and more.

### 🧪 Machine Learning Toolkit
- **📉 ML Algorithm Comparator (LazyRegressor)**: Compare multiple regression algorithms side-by-side with performance metrics like R², RMSE, MAE, and execution time.
- **🔧 Hyperparameter Tuning**: Perform hyperparameter optimization on selected ML algorithms using GridSearchCV or RandomizedSearchCV.

### 📂 Excel Utilities
- **🧾 Excel File Merger**: Upload and merge multiple Excel files (with identical or different structures) into a single DataFrame.

---

## 💡 Use Cases

- 📚 Learn how different ML models perform on your dataset.
- 📊 Visualize datasets without writing code.
- 🤖 Generate SQL queries from plain English.
- 📈 Automatically analyze uploaded datasets with EDA.
- 🔍 Tune models with ease and select the best one.
- 📂 Merge and prepare Excel data for reporting or analysis.

---

## 🛠 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Libraries**:
  - `pandas`, `numpy` – Data handling
  - `plotly`, `matplotlib`, `seaborn` – Visualization
  - `scikit-learn`, `lazyregression`, `xgboost` – ML
  - `streamlit_pandas_profiling`, `sweetviz` – EDA
  - `sqlalchemy`, `sqlite3`, `langchain` – SQL generator
  - `openai/groq` – Natural Language to SQL (if integrated)

---

