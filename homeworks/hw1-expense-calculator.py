"""
Personal Finance Calculator
Student: Aemamorn Sudprasong
Date: 27/07/2568
Purpose: Calculate monthly budget and savings
"""

# รับข้อมูลจากผู้ใช้
monthly_income = float(input("Enter your monthly income (THB): "))
rent_cost = float(input("Enter your monthly rent/housing (THB): "))
food_budget = int(input("Enter your monthly food budget (THB): "))
transportation_cost = float(input("Enter your monthly transportation expenses (THB): "))
entertainment_budget = int(input("Enter your monthly ententainment budget (THB): "))
emergency_fund_percent = float(input("Enter percentage to save for emergency (e.g.,10.5): "))
investment_percent = float(input("Enter Percentage to invest (e.g.,15.0): "))

#คำนวณค่าใช่จ่ายคงที่
total_fixed_expenses = rent_cost + transportation_cost

#คำนวณค่าใช้จ่ายไม่คงที่
total_variable_expenses = food_budget + entertainment_budget

#คำนวณเงินเผื่อสำหรับฉุกเฉินและลงทุน
emergency_fund = monthly_income * (emergency_fund_percent / 100)
investment_fund = monthly_income * (investment_percent / 100)

#คำนวณค่าใช้จ่ายทั้งหมด
total_expenses = total_fixed_expenses + total_variable_expenses

#คำนวณรายได้คงเหลือ
remaining_income = monthly_income - total_expenses

#คำนวณเงินเหลือออม
available_for_savings = remaining_income - emergency_fund - investment_fund

#คำนวณสัดส่วนค่าใช้จ่ายต่อรายได้
expenses_ratio = (total_expenses / monthly_income) * 100

#แสดงผลลัพธ์
print("\n=== MONTHLY BUDGET REPORT ===")
print(f"Income:{monthly_income:.2f}THB")
print(f"Fixed Expenses:{total_fixed_expenses:.2f}THB")
print(f"Variable Expenses:{total_variable_expenses:.2f}THB")
print(f"Total Expenses:{total_expenses:.2f}THB")
print(f"Remaining:{remaining_income:.2f}THB")

print("\n=== SAVING BREAKDOWN ===")
print(f"Emergency Fund ({emergency_fund_percent}%):{emergency_fund:.2f}THB")
print(f"Investment({investment_percent}%):{investment_fund:.2f}THB")
print(f"Available for Savings:{available_for_savings:.2f}THB")

print("\n=== ANALYSIS ===")
print(f"Expense Ratio:{expenses_ratio:.2f}%\n\n")