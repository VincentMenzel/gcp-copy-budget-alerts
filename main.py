from google.cloud.billing.budgets import BudgetServiceClient

# Global Variables
SOURCE_BILLING_ACCOUNT_ID = "YOUR_SOURCE_BILLING_ACCOUNT_ID"
TARGET_BILLING_ACCOUNT_ID = "YOUR_TARGET_BILLING_ACCOUNT_ID"


def copy_budgets():
    client = BudgetServiceClient()

    # Construct the billing account name for the source
    source_account_name = f"billingAccounts/{SOURCE_BILLING_ACCOUNT_ID}"
    target_account_name = f"billingAccounts/{TARGET_BILLING_ACCOUNT_ID}"

    # List all budgets in the source billing account
    budgets = client.list_budgets(parent=source_account_name)

    for budget in budgets:
        # Clear etag since this is an update
        del budget.etag

        # Create the budget in the new billing account
        client.create_budget(parent=target_account_name, budget=budget)
        print(f"Copied budget: {budget.display_name}")


if __name__ == "__main__":
    copy_budgets()
