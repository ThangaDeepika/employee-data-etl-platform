# Employee Data ETL Platform

## Overview

An end-to-end ETL platform built using Python, Pandas, MySQL, FastAPI, and Streamlit.

This project reads employee Excel files from nested folders, validates and cleans data, removes duplicates, loads valid records into MySQL, captures audit and error logs, exposes APIs using FastAPI, and visualizes results through an interactive Streamlit dashboard.

---

## Architecture

```text
Excel Files
      ↓
ETL Pipeline
      ↓
Validation & Cleaning
      ↓
MySQL Database
      ↓
FastAPI REST APIs
      ↓
Streamlit Dashboard
```

---

## Features

✅ Recursive Excel File Scanning

✅ Data Validation

✅ Duplicate Detection

✅ Null Value Detection

✅ Invalid Age Validation

✅ Negative Salary Validation

✅ Data Cleaning

✅ MySQL Integration

✅ Error Logging

✅ Audit Logging

✅ FastAPI Backend

✅ Streamlit Dashboard

---

## Technology Stack

- Python
- Pandas
- MySQL
- FastAPI
- Streamlit
- OpenPyXL
- REST APIs

---

## Dashboard Modules

### Dashboard

Displays:

- Unique Employees
- Files Processed
- Rows Read
- Valid Records
- Duplicate Records
- Validation Errors

### Employees

Displays cleaned employee data loaded into MySQL.

### Errors

Displays validation failures detected during ETL processing.

### Audit

Displays file-level processing summaries and ETL statistics.

---

## Project Structure

```text
ETL_App

├── backend
│   ├── api
│   ├── config
│   ├── database
│   ├── pipeline
│   └── services
│
├── frontend
│   ├── app.py
│   └── pages
│
├── logs
│
├── requirements.txt
└── README.md
```

---

## ETL Flow

```text
Excel Files
      ↓
File Scanner
      ↓
Validation
      ↓
Cleaning
      ↓

Valid Records
      ↓
employee_data

Invalid Records
      ↓
error_log

Processing Summary
      ↓
audit_log

      ↓

FastAPI

      ↓

Streamlit Dashboard
```

---

## Author

### Thanga Deepika R

Graduate Engineer Trainee

Built as a learning project to understand ETL architecture, data validation, database integration, API development, and dashboard reporting.