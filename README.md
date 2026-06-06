# Solar CRM System

## Overview

Solar CRM is a web-based Customer Relationship Management (CRM) system developed specifically for solar energy companies. The system helps manage the complete customer lifecycle from lead generation to after-sales support.

The application centralizes customer information, quotations, projects, invoices, site surveys, inventory, employees, and support tickets into a single platform.

---

## Project Information

**Project Title:** Solar CRM System

**Developed By:** Satyarajsinh Jadeja

**Enrollment Number:** 2302031800032

**College:** Aditya Silver Oak Institute of Technology

**University:** Silver Oak University

**Semester:** 7

**Academic Year:** 2026-27

**Internship Organization:** Enjay IT Solutions

**Internship Duration:** May 2026 – June 2026

**Location:** Bhilad, Vapi

---

# Technology Stack

## Frontend

- HTML5
- CSS3
- JavaScript
- Bootstrap 5
- Font Awesome

## Backend

- Python
- Django Framework

## Database

- SQLite

## Development Tools

- Visual Studio Code
- Git
- GitHub

---

# Features

## Dashboard

- Lead Statistics
- Customer Statistics
- Project Statistics
- Ticket Statistics
- Recent Activities

---

## Lead Management

- Add Lead
- Edit Lead
- View Lead
- Delete Lead
- Assign Lead to Employee
- Lead Status Tracking

### Lead Workflow

New → Contacted → Qualified → Won / Lost

---

## Follow-Up Management

- Schedule Follow-Ups
- Track Customer Communication
- Update Follow-Up Status
- Employee Assignment

### Status

- Pending
- Done

---

## Customer Management

- Customer Records
- Contact Information
- Address Details
- Customer History

---

## Site Survey Management

- Roof Inspection
- Survey Reports
- Site Feasibility Analysis
- Solar Capacity Recommendations

---

## Product & Inventory Management

- Add Products
- Inventory Tracking
- Stock Management
- Stock Adjustment

### Product Examples

- Solar Panels
- Inverters
- Batteries
- Mounting Structures

---

## Quotation Management

- Create Quotations
- Add Multiple Products
- Automatic GST Calculation
- Government Subsidy Calculation
- Discount Management
- PDF Generation

### Quotation Features

- Product Wise Pricing
- GST Calculation
- Subsidy Deduction
- Discount Calculation
- Final Amount Calculation

---

## Project Management

- Create Projects
- Assign Customers
- Track Progress
- Manage Installation Activities

### Project Status

- Planning
- In Progress
- Completed
- On Hold

---

## Invoice Management

- Generate Invoices
- Payment Tracking
- Invoice PDF Printing
- Customer Billing

### Invoice Status

- Paid
- Unpaid
- Overdue

---

## Employee Management

- Add Employees
- Manage Accounts
- Assign Work
- Role-Based Access

### Roles

#### Administrator

Full Access

#### Employee

Limited Access

- Assigned Leads
- Assigned Customers
- Assigned Projects
- Assigned Quotes
- Assigned Tickets

---

## Import Leads

- CSV Import
- Excel Import
- Bulk Lead Upload

---

## Customer Ticket Portal

Customers can:

- Verify Email
- Receive OTP
- Raise Support Ticket
- Get Ticket Number
- Receive Email Confirmation

---

## Ticket Management

Administrators can:

- View Tickets
- Assign Tickets
- Update Status
- Add Resolution Notes
- Close Tickets

### Ticket Status

- Open
- In Progress
- Resolved
- Closed

---

# User Roles & Permissions

## Admin

Access To:

- Dashboard
- Leads
- Follow Ups
- Customers
- Site Surveys
- Products
- Quotes
- Projects
- Invoices
- Employees
- Import Leads
- Tickets

---

## Employee

Can Access:

- Assigned Leads
- Assigned Follow-Ups
- Assigned Customers
- Assigned Projects
- Assigned Quotes
- Assigned Tickets

Cannot Access:

- Employee Management
- Global System Settings
- Other Employee Data

---

# Security Features

- Django Authentication
- Role-Based Access Control
- CSRF Protection
- Session Management
- OTP Verification
- Secure Login System

---

# Business Workflow

Lead Generated

↓

Lead Added

↓

Follow-Up Process

↓

Customer Conversion

↓

Site Survey

↓

Quotation Creation

↓

Customer Approval

↓

Project Creation

↓

Installation

↓

Invoice Generation

↓

After Sales Support

↓

Ticket Resolution

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
cd solar-crm
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

## Install Requirements

```bash
pip install -r requirements.txt
```

## Apply Migrations

```bash
python manage.py migrate
```

## Create Superuser

```bash
python manage.py createsuperuser
```

## Run Development Server

```bash
python manage.py runserver
```

## Open Browser

```text
http://127.0.0.1:8000/
```

---

# Learning Outcomes

Through this project I learned:

- Django Development
- Database Design
- CRM Workflows
- Authentication Systems
- OTP Integration
- Role-Based Access Control
- Inventory Management
- PDF Generation
- Solar Industry Business Process

---

# Future Scope

- WhatsApp Integration
- SMS Notifications
- Mobile Application
- AI-Based Lead Scoring
- Online Payment Gateway
- Customer Self-Service Portal
- Solar Monitoring Dashboard
- Advanced Analytics

---

# Conclusion

Solar CRM successfully automates the complete solar business lifecycle from lead generation to customer support. The system improves operational efficiency, customer service quality, and business management by centralizing all operations into a single platform.

---

# License

This project was developed for educational and internship purposes.

© 2026 Satyarajsinh Jadeja