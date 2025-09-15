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

### ❌ Error: 'dict' object has no attribute 'extend'

**Problem:** The app installation fails during the hooks loading phase with the error: `AttributeError: 'dict' object has no attribute 'extend'`

**Root Cause:** Some hooks in `hooks.py` are configured as dictionaries when Frappe expects them to be lists. This commonly happens with hooks like:
- `website_generators`
- `clear_cache`
- `boot_session`
- `standard_doctypes`
- Other hooks that should be lists but are defined as dictionaries

**Solution Applied:**
1. ✅ Validated all hook configurations in `hooks.py`
2. ✅ Ensured list hooks are defined as lists `[]`
3. ✅ Ensured dict hooks are defined as dictionaries `{}`
4. ✅ Fixed `website_route_rules` format
5. ✅ Added comprehensive documentation and examples

**Quick Fix:**
If you see this error, check your `hooks.py` file and ensure:
- All hooks expecting lists are defined as `[]` not `{}`
- `website_route_rules` is a list of dictionaries
- No hooks are mixing list/dict formats

### Installation Commands

For a fresh Frappe site installation:

```bash
# Install the app in your bench (fixed version)
bench get-app https://github.com/macrobian88/airport-automation.git --branch fix-hooks-extend-error

# Install the app on your site
bench --site your-site-name install-app airplane_mode

# Optional: Migrate if needed
bench --site your-site-name migrate
```

### Diagnostic Tool

We've included a hooks validator script to help diagnose configuration issues:

```bash
# Run the validator on your hooks.py file
python validate_hooks.py airplane_mode/hooks.py

# Or just run it from the app directory
python validate_hooks.py
```

This will check for common configuration issues and provide specific fixes.

### Alternative Installation (if using the original repo)

```bash
# Clone the repository
git clone https://github.com/younis-ali/airport-automation.git
cd airport-automation

# Check out the fixed branch or apply the fix manually
# Edit airplane_mode/hooks.py and fix the following:
# 1. Change: # required_apps = []
#    To: required_apps = []
# 
# 2. Ensure all hooks expecting lists are defined as lists []
# 3. Ensure website_route_rules is properly formatted as list of dicts

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

## Common Hook Configuration Issues

### List Hooks (must be lists [])
These hooks should always be defined as lists:
```python
required_apps = []
website_generators = ["Flights"]
clear_cache = ["airplane_mode.utils.clear_cache"]
boot_session = ["airplane_mode.utils.boot_session"]
auth_hooks = ["airplane_mode.auth.validate"]
```

### Dict Hooks (must be dictionaries {})
These hooks should be defined as dictionaries:
```python
doc_events = {
    "Flights": {
        "on_update": "airplane_mode.doctype.flights.flights.sync_gate_number"
    }
}

scheduler_events = {
    "daily": ["airplane_mode.tasks.daily"]
}
```

### List of Dicts (must be list containing dictionaries)
```python
website_route_rules = [
    {"from_route": "/show-me", "to_route": "show_me"}
]
```

## Verification

After successful installation, verify the app is working:

1. Log into your Frappe site
2. Check that Airplane Mode appears in the app list
3. Navigate to the doctypes: Airlines, Airplanes, Airports, Flights, etc.
4. Create test records to ensure functionality

## Support

If you encounter any other installation issues:
1. Run the hooks validator: `python validate_hooks.py`
2. Check the bench logs: `bench logs`
3. Verify your Frappe version compatibility
4. Ensure all prerequisites are met for Frappe development

## Error Patterns

### Pattern 1: extend() error
```
AttributeError: 'dict' object has no attribute 'extend'
```
**Solution:** Check hooks.py for hooks defined as `{}` that should be `[]`

### Pattern 2: Required app not found
```
Required app not found 'airplane_mode', 'erpnext'
```
**Solution:** Uncomment `required_apps = []` in hooks.py

### Pattern 3: Import errors during installation
```
ImportError: No module named 'airplane_mode.something'
```
**Solution:** Check that all referenced modules exist and paths are correct

This guide covers the major installation issues and their fixes. The updated repository includes all these fixes and diagnostic tools.
