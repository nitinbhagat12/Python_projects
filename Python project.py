print("Welcome to UNIVERSAL CURRENCY CALCULATOR ")

print("The current currencies and their rates available are: " )

print("Currency                    CODE              Rate in INR ")
print("Indian national rupees      INR               Rs.1")
print("Euro                        EUR               Rs.81 ")
print("United States Dollar1       USD               Rs.82 ")
print("Swiss Franc                 CHF               Rs.82")
print("British Pound               GBP               Rs.93")
print("Gibraltar Pound             GIP               Rs.95")
print("Cayman Island Dollar        KYD               Rs.99")
print("Jordanian Dinar             JOD               Rs.116")
print("Omani Rial                  OMR               Rs.214")
print("Bahraini Dinar              BHD               Rs.219")
print("Kuwaiti Dinar               KWD               Rs.266")

INR=1
EUR=81
USD=82
CHF=82
GBP=93
GIP=95
KYD=99
JOD=116
OMR=214
BHD=219
KWD=266
print("This is to convert amount from any of the following currencies to INR") 
a=str(input("Enter the currency code you want to convert to INR: "))
b=int(input("Enter the amount in the respective currency: "))

if a=="EUR":
      print("The final amount in INR is: ",b*EUR)
elif a=="USD":
      print("The final amount in INR is: ",b*USD)
elif a=="CHF":
      print("The final amount in INR is: ",b*CHF)
elif a=="GBP":
      print("The final amount in INR is: ",b*GBP)
elif a=="GIP":
      print("The final amount in INR is: ",b*GIP)
elif a=="KYD":
      print("The final amount in INR is: ",b*KYD)
elif a=="JOD":
      print("The final amount in INR is: ",b*JOD)
elif a=="USD":
      print("The final amount in INR is: ",b*USD)
elif a=="OMR":
      print("The final amount in INR is: ",b*OMR)
elif a=="BHD":
      print("The final amount in INR is: ",b*BHD)
elif a=="KWD":
      print("The final amount in INR is: ",b*KWD)
else:
      print("Please check the the currency code")
print("Thankyou for using our Currency calculator")
      
      

