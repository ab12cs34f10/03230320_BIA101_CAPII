class Employee:
    def _init_(self, name, income, position, organization):
        # this codes initializes the details of employees
        self._name = name  
        self._income = income 
        self._position = position  
        self._organization = organization  

class TaxCalculator:
    def _init_(self, employee):
        # This code helps to initialize the taxCalculator as per the asnwers of employees
        self._employee = employee  
        
        self._taxable_income = self._calculate_taxable_income()  # taxable income are obtaind by this code
        self._tax_amount = self._calculate_tax_amount()  # amount of tax is calculated by this code

    def _calculate_taxable_income(self):
        # This codes calculates taxable income based on employee's income and position
        taxable_income = self._employee._income

        #This code aids to deduct the decutable income of employees
        if self._employee._position == "Regular":
            taxable_income -= 0.10 * self._employee._income  # 10% of PF (Provident Fund) is deducted by this code
            taxable_income -= 0.05 * self._employee._income  # 5% Group Insurance Scheme will be deducted from the employees income

        # General deduction of income as per the income Act of Bhutan
        general_deductions = min(0.05 * taxable_income, 350000)  # By rules of tax act of bhutan 5% or 350,000 of income, whichever is lower will be deducted
        taxable_income -= general_deductions

        return taxable_income

    def _calculate_tax_amount(self):
        # this codes defines general tax rates of income per year of individuals 
        tax_rates = [
            (300000, 0.0),
            (400000, 0.10),
            (650000, 0.15),
            (1000000, 0.20),
            (1500000, 0.25),
            (float('inf'), 0.30)
        ]

        # This code helps to calculate the amount of tax based on above provided tax rate of bhutan per annum
        tax_amount = 0
        for rate, rate in tax_rates:
            if self._taxable_income <= 0:
                break
            if self._taxable_income > rate:
                tax_amount += rate * rate  # Calculate tax amount for current slab/ rate
                self._taxable_income -= rate  # Deduct current slab from taxable income
            else:
                tax_amount += self._taxable_income * rate  # Calculate tax amount for remaining income
                break

        # Apply surcharge if applicable (10% surcharge if tax amount >= 1,000,000)
        if tax_amount >= 1000000:
            tax_amount += 0.10 * tax_amount  # Apply 10% surcharge

        return tax_amount

try:
    # ask the employee details on terminal
    name = input("Enter employee's name: ")
    income = float(input("Enter employee's income: "))
    position = input("Enter employee's position (Regular/Non-Regular): ").capitalize() 
    organization = input("Enter employee's organization: ")

    emp_1 = Employee(name, income, position, organization)
    
    if emp_1._income < 300000:
        # Inform employee if they're not liable for taxes (income below taxable income as per the rules of tax Act)
        print(f"{emp_1._name}, you are not liable for taxes as the income is below the taxable threshold.")
    else:
        # this code helps to calculate tax amount for eligible employees(,300,000)
        calculator = TaxCalculator(emp_1)
        print(f"Tax amount for {emp_1._name}: Nu. {calculator._tax_amount:.2f}")
except ValueError:
    # Handle invalid input for income
    print("Please enter a valid numerical value for income.")
except Exception as e:
    # Handle any other exceptions
    print("An error occurred:", str(e))