# Installation Troubleshooting Guide

This document provides solutions to common installation issues with the Airplane Mode app.

## Fixed Issues

### ❌ Error: Required app not found 'airplane_mode', 'erpnext'

**Problem:** The app was failing to install with a dependency error, specifically mentioning that 'airplane_mode' and 'erpnext' were not found.

**Root Cause:** The `required_apps` parameter in `hooks.py` was commented out, causing Frappe's dependency resolution system to fail during installation.

**Solution Applied:**
1. ✅ Uncommented the `required_apps` parameter in `airplane_mode/hooks.py`
2. ✅ Set `required_apps = []` to indicate this is a standalone app
3. ✅ Added proper documentation about dependency management

### Installation Commands

For a fresh Frappe site installation:

```bash
# Install the app in your bench
bench get-app https://github.com/macrobian88/airport-automation.git

# Install the app on your site
bench --site your-site-name install-app airplane_mode

# Optional: Migrate if needed
bench --site your-site-name migrate
```

### Alternative Installation (if using the original repo)

```bash
# Clone the repository
git clone https://github.com/younis-ali/airport-automation.git
cd airport-automation

# Check out the fixed branch or apply the fix manually
# Edit airplane_mode/hooks.py and uncomment the required_apps line:
# Change: # required_apps = []
# To: required_apps = []

# Then install
bench get-app ./
bench --site your-site-name install-app airplane_mode
```

## Additional Notes

- This app is designed to work as a standalone Frappe application
- ERPNext is NOT required for this app to function
- If you need ERPNext integration, you can add it to the `required_apps` list in hooks.py

## Dependencies Management

The app currently has minimal dependencies:
- **Frappe Framework** (automatically handled by bench)
- **No ERPNext dependency** (can be added if needed)

If you need to add dependencies in the future, modify the `required_apps` list in `airplane_mode/hooks.py`:

```python
# Example: Adding ERPNext as a dependency
required_apps = ["erpnext"]

# Example: Adding multiple dependencies
required_apps = ["erpnext", "other_app"]
```

## Verification

After successful installation, verify the app is working:

1. Log into your Frappe site
2. Check that Airplane Mode appears in the app list
3. Navigate to the doctypes: Airlines, Airplanes, Airports, Flights, etc.
4. Create test records to ensure functionality

## Support

If you encounter any other installation issues:
1. Check the bench logs: `bench logs`
2. Verify your Frappe version compatibility
3. Ensure all prerequisites are met for Frappe development

This fix resolves the primary installation dependency issue that was preventing the app from being installed on fresh Frappe sites.
