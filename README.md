<p align="center">
    <img width="600" src="https://drive.google.com/uc?id=1K0psj5n-OoLHwowFkd0qegfuYNSB5XOV">
</p>

# 🚗 Fleet Inspections

Fleets is a modern web application designed to help companies efficiently track fleet inspections, issues, and maintenance.  
The motivation came from seeing traditional paper-based inspections at my company—making it tedious to track vehicle maintenance and usage.  
This app was inspired by the CS50 Week 9 "finance" project and is built with Flask.

---

## Features

- **User-friendly web interface** for inspection and maintenance tracking
- **Roles and permissions**: Owner, Admin, and User with distinct access levels
- **Vehicle management**: Add, edit, or scan vehicle VINs (barcode scanning support)
- **Inspection tracking**: Digital checklists with automatic prompts for issues
- **Maintenance projections**: Upcoming maintenance alerts and visual graphs
- **Responsive design**: Usable on desktop and mobile devices
- **Basic automated tests** for main workflows

---

## 📦 Requirements

- Python 3.x
- Flask
- Flask-Session

Install requirements:
```bash
pip install flask flask-session
```

---

## 🚀 Getting Started

1. **Install the app as a module:**
    ```bash
    pip install -e .
    ```
    _(Run this in your project’s root folder.)_

2. **Run with Flask CLI:**
    ```bash
    export FLASK_APP="fleets"
    flask run
    ```

    Or run the app instance directly:
    ```bash
    cd fleets
    python3 myapp.py
    ```

3. **Deploying on a WSGI Server:**
    Add this to your server config:
    ```python
    import sys
    path = 'path/to/project/folder/fleets/'
    if path not in sys.path:
        sys.path.append(path)

    from myapp import app as application
    ```

---

## 🧪 Running Tests

Basic tests are included for authentication, users, vehicles, inspections, and database operations.

Install test requirements:
```bash
pip install pytest coverage
```

Run tests:
```bash
pytest
```

Sample output:
```
================================== test session starts ==================================
platform linux -- Python 3.6.9, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /home/angel/repos/fleet-inspections, configfile: setup.cfg, testpaths: tests
collected 128 items                                                                     

tests/test_auth.py ..............                                                 [ 10%]
tests/test_db.py ..                                                               [ 12%]
tests/test_factory.py ..                                                          [ 14%]
tests/test_inspec.py ...................                                          [ 28%]
tests/test_pass.py .....................                                          [ 45%]
tests/test_users.py ..............................                                [ 68%]
tests/test_vehicles.py ........................................                   [100%]

================================= 128 passed in 26.29s ==================================
```

---

## 🌐 Usage Overview

The app is live (for demo) at: [angelelz.pythonanywhere.com](https://angelelz.pythonanywhere.com/)

### Register

- Company owner registers an account with company name, username, email, and password.
- Both client-side and server-side validation for all inputs.
- Errors are displayed as alerts and user input is preserved during correction.

<p align="center">
<img width="800" src="https://drive.google.com/uc?id=1Axom-A8HbpH_8L8BdGtbafYMlhiS5PA2">
</p>

---

### Logging In

- Owners log in with their credentials.
- The dashboard displays users and vehicles in the company.
- Tables are responsive and adapt to mobile screens.
- VIN data can be random for demo purposes.

<p align="center">
<img width="800" src="https://drive.google.com/uc?id=1AyaTfE0i5thiQgMlmUtSKJoTiz5CEAmW">
<img width="300" src="https://drive.google.com/uc?id=1B50uVBAE3N-5hUNvQxL84cBBr9j-rbYF">
</p>

---

### User Roles

- **Owner:** One per company (created at registration)
- **Admin:** Has same permissions as owner
- **User:** Cannot add/edit users or see vehicles tracking/inspection data

Example view for a user:
<img width="800" src="https://drive.google.com/uc?id=1B9EtWtatD1rJqMm8EI9_gYzddqzzwBtQ">

Owners/Admins can add/edit users via the navigation dropdown:
<img width="800" src="https://drive.google.com/uc?id=1B8wOZLp95-LEEcyCbTUS2SXAVz4eCNvM">

---

### Vehicle Management

- Add/edit vehicles via the navigation menu
- All fields required except the tag
- Optionally scan VIN barcode using [QuaggaJS](https://serratus.github.io/quaggaJS/) with your phone camera

<img width="800" src="https://drive.google.com/uc?id=1B9PDAiv6ECfRWE-OVz1X3vXXc2ZxbAuK">

---

### Inspections

- Single checklist template, based on real inspection sheet
- All fields required
- Extra notes appear when an item is marked "not ok"

<img width="800" src="https://drive.google.com/uc?id=1BNlB7IBVRuwWFvKbHpC5hUTyqMqQwkEy">

---

### Vehicle Issues & Maintenance Projections

#### All Vehicles

- Owners/Admins can view all vehicles, latest inspection dates, mileage, and next oil change projection
- Overdue vehicles are highlighted in red

<img width="600" src="https://drive.google.com/uc?id=1BOwxyDwcQN2XfLjE1IxLarTmC5SCP78y">

- Interactive graph shows last 8 inspections and oil change projections for each vehicle, powered by [Chart.js](https://www.chartjs.org/)

#### Single Vehicle

- Click any vehicle row to view details and the latest 8 inspections (with issues)
- Graph updates to show only the selected vehicle

<img width="600" src="https://drive.google.com/uc?id=1BWUH0fKSbhsoaMy6Xj8vOsoF1wgEBS8k">

---

## 📬 Feedback

Feel free to open issues or pull requests for suggestions, improvements, or bugfixes.  
If you find this project helpful, a star ⭐️ is appreciated!
