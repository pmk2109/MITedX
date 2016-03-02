"""
PROBLEM 2: PAYING DEBT OFF IN A YEAR  (15 points possible)
Now write a program that calculates the minimum fixed monthly payment needed in order pay
 off a credit card balance within 12 months. By a fixed monthly payment, we mean a single
 number which does not change each month, but instead is a constant amount that will be 
 paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay off all 
debt in under 1 year, for example:

Lowest Payment: 180 
Assume that the interest is compounded monthly according to the balance at the end of the 
month (after the payment for that month is made). The monthly payment must be a multiple 
of $10 and is the same for all months. Notice that it is possible for the balance to 
become negative using this payment scheme, which is okay. A summary of the required 
math is found below:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x 
Monthly unpaid balance)
"""


"""
Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0
"""


balance = 3329
annualInterestRate = 0.2
	
	
mInterestRate = annualInterestRate / 12.0
mLower = balance / 12
mHigher = (balance * (1+mInterestRate)**12) / 12.0
ans = (mLower + mHigher) / 2
epsilon = 0.01
currentBalance = balance

while abs(0 - currentBalance) >= epsilon:
	currentBalance = balance
	previousBalance = balance
	month = 1
	
	while month < 13:
		monthlyUnpaidBalance = previousBalance - ans
		currentBalance = monthlyUnpaidBalance + (mInterestRate * monthlyUnpaidBalance)
		previousBalance = currentBalance
		month+=1
		#print("Month: " + str(month) + ";  Balance: " + str(currentBalance)) + ";  Ans: " + str(ans)

	if (currentBalance > 0):
		mLower = ans
	elif (currentBalance < 0):
		mHigher = ans
		
	ans = (mHigher + mLower) / 2
	
	
print("Lowest payment: " + str(round(ans,2)))
	
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	      
"""	      
totalPaid = 0
minMonthly = 0
monthlyInterest = annualInterestRate / 12.0
currentBalance = balance

while currentBalance > 0:
	currentBalance = balance
	previousBalance = balance
	month = 1
	minMonthly += 10
	print("**********   Lowest Payment: " + str(minMonthly) + "************")
	
	while month < 13:
		monthlyUnpaidBalance = previousBalance - minMonthly
		currentBalance = monthlyUnpaidBalance + (monthlyInterest * monthlyUnpaidBalance)
		previousBalance = currentBalance
		month+=1
		print("Month: " + str(month) + ";  Balance: " + str(currentBalance))

print("Lowest Payment: " + str(minMonthly))
"""







"""
for month in range(12):
	print "Month: " + str(month+1)
	previousBalance = balance
	
	minimumMonthlyPayment = (monthlyPaymentRate * balance)
	monthlyInterest = annualInterestRate / 12.0
	monthlyUnpaidBalance = previousBalance - minimumMonthlyPayment
	balance = monthlyUnpaidBalance + (monthlyInterest*monthlyUnpaidBalance)
	totalPaid = totalPaid + minimumMonthlyPayment
	
	print "Minimum monthly payment: " + str(round(minimumMonthlyPayment,2))
	print "Remaining balance: " + str(round(balance,2))
	
	
print "Total paid: " + str(round(totalPaid,2))
print "Remaining balance: " + str(round(balance,2))	

"""

