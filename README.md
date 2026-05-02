# CIW Claim Search Automation

Python automation script for performing claim searches on the CIW (Claims Inquiry Web) portal.

The script logs into the portal, navigates the claim search interface using Selenium, retrieves claim details, and generates a CSV report for multiple claim IDs.

## Features

- Automated login to CIW portal
- Dynamic UI navigation using Selenium
- Hover interaction to reveal hidden claim search options
- Automatic claim search using Claim ID
- Extraction of claim details from web pages
- CSV report generation for multiple claims

## Technologies Used

- Python
- Selenium
- PyAutoGUI
- CSV / Data Processing

## Workflow

```mermaid
flowchart TD
    A[Input Claim IDs] --> B[Python Selenium Script]
    B --> C[Login to CIW Portal]
    C --> D[Hover to Reveal Search Options]
    D --> E[Enter Claim ID]
    E --> F[Search Claim]
    F --> G[Extract Claim Details]
    G --> H[Generate CSV Report]
