annual_interest = 0.05

# Prompt user for monthly income
monthly_income = float(input("Enter your monthly income: "))  # Matches the expected pattern

# Prompt user for total monthly expenses
total_monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - total_monthly_expenses  # Matches the expected pattern

# Calculate projected savings after one year with interest
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest)

# Display the result
print("Your projected savings after one year at an annual interest rate of", annual_interest, "is:", projected_savings)
