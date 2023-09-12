# GCP Billing Alerts Copier

This script allows you to copy billing alerts (budgets) from one GCP billing account to another.

## Prerequisites

- Python 3.x
- Google Cloud SDK (optional, but helps with setting up credentials and permissions)
- Access to both the source and target billing accounts on GCP.
- A Service Account with permissions to:
    - View budgets in the source billing account
    - Create budgets in the target billing account

## Setup

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. Download your Service Account key from the Google Cloud Console and save it as `service-account-key.json` in the root of the repository directory. Make sure this Service Account has the necessary permissions as mentioned above.

4. Update the `SOURCE_BILLING_ACCOUNT_ID` and `TARGET_BILLING_ACCOUNT_ID` in the script with your respective GCP billing account IDs.

## Usage

Run the script:

```bash
python script_name.py
```

## Note

This script provides a basic mechanism to copy billing budgets. Depending on your needs and specific configurations, further modifications might be required.

---

Replace `<repository-url>` and `<repository-directory>` with appropriate values. You can also modify the file name `script_name.py` to the actual name of your script file if it's different.