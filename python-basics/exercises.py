# Print
print "hello world by Thibault"

# Condition control
x = 5
if x > 18:
  print("here is a big boy")
else:
  print("here is a small boy")

# Loop
n = 5
while n > 0:
  print n
  n -= 1
print "Finish"

# User input & conversion
hrs = float(raw_input("Enter Hours:"))
rate = float(raw_input("Enter Rate:"))
print hrs*rate

# Conditional 1
weekHourLimit = 40
bonusHourLimit = 1.5
hrsI = raw_input("Enter Hours:")
rateI = raw_input("Enter Rate:")
hrs = float(hrsI)
rate = float(rateI)
if hrs <= weekHourLimit:
    pay = hrs * rate
else:
    pay = weekHourLimit * rate + (hrs - weekHourLimit) * rate * bonusHourLimit
print pay

# Conditional 2
outm = "The score is out of range"
try:
    scoreI = raw_input("Enter Score: ")
    score = float(scoreI)
except:
    print "Error: The score is not a number"
if score < 0.0:
    grade = outm
elif score < 0.6:
    grade = "F"
elif score < 0.7:
    grade = "D"
elif score < 0.8:
    grade = "C"
elif score < 0.9:
    grade = "B"
elif score <= 1.0:
    grade = "A"
else:
    grade = outm
print grade

scoreI = raw_input("Enter Score: ")
try:
    score = float(scoreI)
    if score < 0.0:
        grade = "The score is out of range"
    elif score < 0.6:
        grade = "F"
    elif score < 0.7:
        grade = "D"
    elif score < 0.8:
        grade = "C"
    elif score < 0.9:
        grade = "B"
    elif score <= 1.0:
        grade = "A"
    else:
        grade = "The score is out of range"
    print grade
except Exception as e:
    print "The score is out of range"
