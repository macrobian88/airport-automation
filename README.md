
# Airport Management System

## 🚨 Installation Fix Available

**Fixed Issue**: Resolved the `Required app not found 'airplane_mode', 'erpnext'` installation error. See [INSTALLATION_TROUBLESHOOTING.md](./INSTALLATION_TROUBLESHOOTING.md) for details.

## Overview

The **Airport Management System** is a frappe application built on the Frappe Framework designed to manage various aspects of an airport's operations, including **Flight and Ticket Management** and **Shop/Tenant Management**. This system streamlines the process of tracking flights, managing flights, tracking shops and tenants, and handling rent payments in a seamless and automated manner.

---

## Features

### 1. **Flight and Ticket Management**

- **Flight Passenger Management**:
  - Create and manage passengers with details like first name, last name, and date of birth.
    
- **Airplane Ticket Management**:
  - Link passengers to tickets with detailed information such as source and destination airports, flight details, departure date and time, and duration of the flight.
  - Fetch source and destination airport codes automatically.
  - Track the status of tickets (Booked, Checked-In, Boarded) with color-coded indicators.
  - Gate numbers are synced across Fligts and Tickets usng doc_event hook

### 2. **Shop and Tenant Management**

- **Shop Management**:
  - Track shops in an airport with details like shop number, name, physical properties (area), and availability status.
  - Link shops to tenants and monitor the status of the shop (available, leased, etc.).

- **Tenant Management**:
  - Store tenant information, including contact details (name, email), and contract details (rent amount, contract start and end dates).
  - Validate tenant email and ensure contract end date is at least one year after the start date.

- **Rent Payment Tracking**:
  - Track rent payments on a monthly basis for each shop and issue rent receipts.
  - Generate rent receipts using Frappe's Print Designer.
  - Send automated monthly rent reminders to tenants via email using scheduled events.

### 3. **Some Reporting**
  1. Shop availibility by ariport
  2. Count shops on the basis of Airport
  3. Count Airplanes by Airport
  4. Compute Revenue by Airline
  5. Show the popular Ad-ons
---

## Installation

### Quick Install (Fixed Version)

```bash
# Install the fixed version from this repository
bench get-app https://github.com/macrobian88/airport-automation.git

# Install on your site
bench --site your-site-name install-app airplane_mode

# Run migrations
bench --site your-site-name migrate
```

### Alternative Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/younis-ali/airport-automation.git
   ```

2. **Set up Frappe and Bench**:
   Follow Frappe's official documentation to install Bench and Frappe framework:
   - https://frappeframework.com/docs/v15.x/user/en/installation

3. **Apply the fix** (if using original repo):
   Edit `airplane_mode/hooks.py` and change:
   ```python
   # required_apps = []
   ```
   to:
   ```python
   required_apps = []
   ```

4. **Install the app**:
   ```bash
   bench get-app .
   bench --site your-site-name install-app airplane_mode
   ```

5. **Run migrations**:
   ```bash
   bench --site your-site-name migrate
   ```

### Troubleshooting

If you encounter the error: `Required app not found 'airplane_mode', 'erpnext'`, see our detailed [Installation Troubleshooting Guide](./INSTALLATION_TROUBLESHOOTING.md).

---

## Usage

- **Flight and Ticket Management**: Add and manage flights, passengers, and tickets from the Desk.
- **Shop Management**: Manage shops, tenants, and rent payments.

---
## Screen Shots
Access flights and book tickets
![image](https://github.com/user-attachments/assets/72f4fbc9-9af4-42c7-bcb7-ed83d0fa8782)

Reports
![image](https://github.com/user-attachments/assets/452fa7cd-9736-4410-ad46-e490216c8e80)

![image](https://github.com/user-attachments/assets/f2d5d409-6c5d-44ee-80ea-845d9c495361)

Shops Web View
![image](https://github.com/user-attachments/assets/a41f8f65-ea9e-48e8-b333-8b6eea81770b)

Rent Payment Receipt with status
![image](https://github.com/user-attachments/assets/6f61918e-f819-4863-8c3e-9b214a671b3d)

## Dependencies

This app is designed to work as a **standalone Frappe application** with minimal dependencies:
- ✅ **Frappe Framework** (automatically handled by bench)
- ❌ **ERPNext NOT required** (can be added if needed)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## Contributors

- Younis (lone.younis1993@gmail.com)
- Fixed installation issues by macrobian88
