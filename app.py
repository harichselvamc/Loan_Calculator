import streamlit as st

class LoanCalculator:
    def __init__(self):
        st.title("Loan Calculator")  # Main title

        # Loan Details
        self.annual_interest_rate = st.number_input("Annual Interest Rate (%)", min_value=0.1, step=0.1, format='%f')
        self.number_of_years = st.number_input("Number of Years", min_value=1, step=1)
        self.loan_amount = st.number_input("Loan Amount", min_value=1, step=1)

        # Initialize attributes
        self.monthly_payment = 0.0
        self.total_payment = 0.0

        # Calculate button
        if st.button("Calculate"):
            self.calculate_loan()

        # Display results
        st.subheader("Loan Calculation Results")
        st.write(f"Monthly Payment: {self.monthly_payment:.2f}")
        st.write(f"Total Payment: {self.total_payment:.2f}")

    def calculate_loan(self):
        monthly_interest_rate = self.annual_interest_rate / 1200
        number_of_payments = self.number_of_years * 12

       
        self.monthly_payment = self.get_monthly_payment(self.loan_amount, monthly_interest_rate, number_of_payments)

        
        self.total_payment = self.monthly_payment * number_of_payments

    def get_monthly_payment(self, loan_amount, monthly_interest_rate, number_of_payments):
        monthly_payment = loan_amount * monthly_interest_rate / (1 - 1 / (1 + monthly_interest_rate) ** number_of_payments)
        return monthly_payment

if __name__ == "__main__":
    LoanCalculator()
