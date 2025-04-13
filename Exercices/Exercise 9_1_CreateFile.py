data = """ empid,empname,emplocation,empsalary
e001,iniyal,chennai,20000.00
e002,aniyal,bangalore,25000.00
e003,indulekha,trivandrum,18000.00 """

with open("data.txt","w") as file:
    file.write(data)


print("file data.txt created successfully")