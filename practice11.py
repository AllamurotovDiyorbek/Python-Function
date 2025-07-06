def calculate_tax(salary: float) -> float:
    if salary>5_000_000:
        salary=salary/100*20
    else:
        salary=salary/100*13
    return salary
def calculate_net_salary(salary: float) -> float:
    return salary-calculate_tax(salary)
salary=10_000_000
tax=calculate_tax(salary)
net_salary=calculate_net_salary(salary)
print(f"Soliq: {tax:,.2f} so`m")
print(f"oylik: {net_salary:,.2f} so`m")