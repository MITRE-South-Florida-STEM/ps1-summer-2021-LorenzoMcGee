#Worked With:
#*Raul Campos
#*Marcos Carillo
def getNumberFromUser(text):
  x = ""
  while(type(x) != type(0.0)):
    try:
        temp = float(input(text))
        x = temp
    except ValueError:
        print("Input must be a number.")
  return x

def incrementCurrentSavings(curSav, r):
  curSav += curSav*(r)/12
  return curSav

def calculateSavings(CurrentSavings,PortionDownPayment,R,PortionSaved,MonthlySalary,AnnualSalary,SemiAnnualRaise,months): 
    x = 0
    while(x < months):
        x += 1
        CurrentSavings = incrementCurrentSavings(CurrentSavings,R)
        CurrentSavings += (PortionSaved*MonthlySalary)
        if x % 6 == 0:
            AnnualSalary *= (SemiAnnualRaise+1)
            MonthlySalary = AnnualSalary/12
    return CurrentSavings


total_cost = 1000000
portion_down_payment = total_cost*0.25
current_savings = 0
r = 0.04
annual_salary = getNumberFromUser("Please input your annual salary: ");
monthly_salary = annual_salary/12
portion_saved = -1
semi_annual_raise = 0.07

targetMonths = 36
iterations = 0
low = 0
high = 10000
mid = (low + high)/2
calculatedSavings = -1
while(calculatedSavings < portion_down_payment - 100 or calculatedSavings > portion_down_payment + 100):
    iterations += 1
    mid = (low + high)/2

    lowDEC = low / 10000.0
    midDEC = mid / 10000.0
    highDEC = high / 10000.0

    calculatedSavings = calculateSavings(current_savings,portion_down_payment,r,mid,monthly_salary,annual_salary,semi_annual_raise,targetMonths)
    
    if(calculatedSavings < portion_down_payment - 100):
        low = mid
    elif(calculatedSavings > portion_down_payment + 100):
        high = mid
mid /= 10
mid = round(mid,4)

print("Best savings rate:",mid)
print("Iterations: ",iterations)
