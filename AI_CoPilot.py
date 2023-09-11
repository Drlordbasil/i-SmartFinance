import time
import requests

API_KEY = "YOUR_API_KEY"
USER = "john_doe"


def make_request(url):
    while True:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as err:
            print(f"Request Exception: {err}")
            time.sleep(5)


url = f"https://api.example.com/financial_data?user={USER}&api_key={API_KEY}"
data = make_request(url)

if data:
    print(f"Your income: {data['income']}")
    print(f"Your expenses: {data['expenses']}")
    print(f"Your savings: {data['savings']}")
    print(f"Your investment portfolio: {data['investment_portfolio']}")
else:
    print("No data found.")

total_expenses = sum(data['expenses'])
savings = data['income'] - total_expenses
print(
    f"Based on your income of {data['income']} and expenses of {total_expenses}, your savings can be {savings}.")

print("Here are some potential cost-cutting measures:")
for expense in data['expenses']:
    if expense > data['income'] * 0.2:
        suggestion = f"Reduce {expense} by 10%"
    else:
        suggestion = f"Cut {expense} by 5%"
    print(suggestion)

profile = "Moderate risk, long-term investor"
print(
    f"Based on your risk tolerance of {data['risk_tolerance']} and investment horizon of {data['investment_horizon']}, your investment profile is {profile}.")

time.sleep(60)
