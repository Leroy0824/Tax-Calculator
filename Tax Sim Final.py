import numpy
#Reference: https://www.gov.uk/government/publications/rates-and-allowances-income-tax/income-tax-rates-and-allowances-current-and-past#tax-rates-and-bands
print("The script was written on 16 Aug 2026. The tax system may change after that date.")
jobincome=float(input("What is your annual income (not including saving and dividend)? "))
income=jobincome
if income>100000:
    allowance=0
else:
    allowance=12570
saving=0
print("The savings are defined as the income generated from the following: \n bank and building society accounts \n savings and credit union accounts \n unit trusts, investment trusts, and open-ended investment companies \n peer-to-peer lending \n trust funds \n payment protection insurance (PPI) \n government or company bonds \n life annuity payments \n some life insurance contracts")
question100=input("Do you have any income from saving? (Yes/No) ")
if question100=="Yes":
    Pass="Fail"
    while Pass!="Pass":
        test=input("Does it involve any joint account? (Yes/No) " )
        if test=="No":
            saving=float(input("How much you gain from savings? "))
            Pass="Pass"
        if test=="Yes":
            num=int(input("How many joint accounts do you have? " ))
            saving=0
            for i in range(1,num+1):
                temp=float(input("How much do you gain from savings in a joint account? "))
                temp2=float(input("How many account holders are on that account? "))
                saving+=(temp/temp2)
                print("We have successfully registered that data.")
            saving2=float(input("How much do you gain from savings that are not in a joint account? "))
            saving+=saving2
            Pass="Pass"
        if test!="No" and test!="Yes":
            print("Please type the answer as “Yes” or “No” only.")
    if income<17570:
        if income<12570:
            if saving>5000:
                allowance+=5000
            else:
                allowance+=saving
        else:
            if saving>(income-12570):
                allowance+=income-12570
            else:
                allowance+=saving
    income+=saving
if question100=="No":
    income+=0
if income>100000:
    allowance=0
    band="Addition"
else:
    if income>37700:
        band="Higher"
    else:
        band="Basic"
    allowance=12570
if band=="Basic":
    if saving>1000:
        allowance+=1000
    else:
        allowance+=saving
if band=="Higher":
    if saving>500:
        allowance+=1000
    else:
        allowance+=saving
print("To claim Blind Person’s Allowance if both of the following apply: \n you’re registered with your local council as blind or severely sight impaired \n you have a certificate that says you’re blind or severely sight impaired (or a similar document from your doctor)")
Pass="Fail"
while Pass!="Pass":
    tests=input("Do you claim Blind Person’s Allowance? (Yes/No) ")
    if tests=="Yes":
        allowance+=3250
        Pass="Pass"
    if tests=="No":
        Pass="Pass"
    if tests!="No" and tests!="Yes":
        print("Please type the answer as “Yes” or “No” only.")
Pass="Fail"
while Pass!="Pass":
    keyq=input("Do you own shares in a company? (Yes/No) ")
    if keyq=="No":
        divide=0
    if keyq=="Yes":
        divide=float(input("How much you earn from dividend? "))
        if divide>500:
            income+=divide
            allowance+=500
        if divide<=500:
            income+=divide
            allowance+=divide
        Pass="Pass"
    if keyq=="No":
        Pass="Pass"
if income>100000:
    allowance=0
    band="Addition"
if income<=100000:
    if income>37700:
        band="Higher"
    else:
        band="Basic"
Personalallocance=input("Are you married or in a civil partnership? (Yes/No) ")
if Personalallocance=="Yes":
    amount1=input("How much do you revive from Married Couple’s Allowance? (Need help? Type help) ")
    if amount1=="help":
        if band=="Basic":
            print("You can receive Marriage Allowance if all the following apply: \n you’re married or in a civil partnership \n your partner do not pay Income Tax or your income is below your Personal Allowance (usually £12,570) \n you pays Income Tax at the basic rate, which usually means your income is between £12,571 and £50,270 before they receive Marriage Allowance")
            print("Important: If yes, your husband, wife or civil partner will transfer £1,260 personal allowance to you. ")
            question=input("Do you receive Marriage Allowance? (Yes/No) ")
            if question=="Yes":
                allowance+=1260
            if question=="No":
                print("Sorry, you cannot claim the marriage allowance based on your answer.")
        else:
            print("Sorry, you cannot claim the marriage allowance based on your income.")
    if amount1!="help":
        allowance+=float(amount1)
    amount2=input("How much do you revive from Marriage Allowance? (Need help? Type help) ")
    if amount2=="help":
        print("You can receiving Married Couple’s Allowance if all the following apply: \n you’re married or in a civil partnership \n you’re living with your spouse or civil partner \n one of you was born before 6 April 1935")
        question1=input("Do you satisfy the last two conditions? (Yes/No) ")
        if question1=="Yes":
            print("You can reduce your tax bill between £436 and £1,127 a year.")
            question2=0
            question2==float(input("How much do you will get? "))
            reducetaxbill=question2
        if question1=="No":
            print("Sorry, you cannot claim the Married Couple’s Allowance based on your answer.")
    if amount2!="help":
        reducetaxbill=float(amount2)
def tax(x):
    if x<37700:
        return x*0.2
    else:
        if x<125140:
            return 37700*0.2+(x-37700)*0.4
        else:
            return 37700*0.2+(125140-37700)*0.4+(x-125140)*0.45
incomeafterallowance=income-allowance-divide
if incomeafterallowance<0:
    tax1=0
    newallowance=-incomeafterallowance
else:
    tax1=tax(incomeafterallowance)
    newallowance=0
def dividetax(x):
    if x<37700:
        return x*0.1075
    else:
        if x<125140:
            return 37700*0.1075+(x-37700)*0.3975
        else:
            return 37700*0.1075+(125140-37700)*0.3575+(x-125140)*0.3935
tax2=tax(divide-newallowance)
tax=tax1+tax2
if tax<0:
    tax=0
print("A for All employees apart from those in groups B, C, H, J, M, V and Z in this table \n B for Married women and widows who have a certificate of election form showing they’re entitled to pay reduced National Insurance \n C for Employees over the State Pension age \n H for Apprentices under 25 \n J for Employees who can defer National Insurance because they’re already paying it in another job \n M for Employees under 21 \n V for Employees who are working in their first job since leaving the armed forces (veterans) \n Z for Employees under 21 who can defer National Insurance because they’re already paying it in another job")
category=input("Which National Insurance category do you fall into? (If not applicable, type N/A) ")
value1=559*12
value2=1048*12
value3=4189*12
if category=="I" or category=="E" or category=="B":
    if income<value1:
        Ni=0
    else:
        if income<value2:
            Ni=0
        else:
            if income<value3:
                Ni=income*0.0185
            else:
                Ni=income*0.02
if category=="C" or category=="K" or category=="S":
    if income<value1:
        Ni=0
    else:
        if income<value2:
            Ni=0
        else:
            if income<value3:
                Ni=0
            else:
                Ni=0
if category=="D" or category=="J" or category=="L" or category=="Z":
    if income<value1:
        Ni=0
    else:
        if income<value2:
            Ni=0
        else:
            if income<value3:
                Ni=income*0.02
            else:
                Ni=income*0.02
if category=="A" or category=="F" or category=="H" or category=="M" or category=="N" or category=="V":
    if income<value1:
        Ni=0
    else:
        if income<value2:
            Ni=0
        else:
            if income<value3:
                Ni=income*0.08
            else:
                Ni=income*0.02
if category=="N/A":
    Ni=0
question6=input("Do you apply to student finance england? (Yes/No): ")
if question6=="Yes":
    question11=input("Do you need to repay for student finance england? (Yes/No) ")
    if question11=="Yes":
        print("If your course start before 1 September 2012, you’re on plan 1 \n If your course start between 1 September 2012 and 31 July 2023, you’ll be on plan 2 if you’re studying an undergraduate course, studying a Postgraduate Certificate of Education (PGCE), take out an Advanced Learner Loan, or take out a Higher Education Short Course Loan. You’ll be on a Postgraduate Loan plan if you’re studying a postgraduate master’s or doctoral course. \n If your course start on or after 1 August 2023, you’ll be on plan 5 if you’re studying an undergraduate course, studying a Postgraduate Certificate of Education (PGCE), take out an Advanced Learner Loan, or take out student finance through your Lifelong Learning Entitlement. You’ll be on a Postgraduate Loan plan if you’re studying a postgraduate master’s or doctoral course. You’ll be on Plan 2 if you take out a Higher Education Short Course Loan.")
        pass1="Fail"
        student=0
        while pass1!="Pass":
            question7=input("Which plan you are on? (1/2/4/5/Postgraduate) ")
            if question7=="1" or question7=="2" or question7=="4" or question7=="5":
                if question7=="1":
                    threshold=26900
                if question7=="2":
                    threshold=29385
                if question7=="4":
                    threshold=33795
                if question7=="5":
                    threshold=25000
                pvalue=0.09
            if question7=="Postgraduate":
                threshold=21000
                pvalue=0.06
            if income>threshold:
                student+=(income-threshold)*pvalue
            else:
                student+=0
            question8=input("Do you also have another student loan plan? (Yes/No) ")
            if question8=="No":
                pass1="Pass"
    if question11=="No":
        student=0
if question6=="No":
    student=0
if question11=="Yes" and question6=="Yes":
    question12=input(f"Do you confirm your balance is greater than or equal to {student}? (Yes/No): ")
    if question12=="Yes":
        student=student
    if question12=="No":
        question13=input("What is the correct amount? ")
        student=float(question13)
print("We estimate the tax to be: £", tax)
print("We estimate the national insurance charged to be: £", Ni)
print("We estimate the student finance charged to be: £", student)
print("We estimate the total income after tax, national insurance, and student finance to be: £", income-tax-Ni-student)