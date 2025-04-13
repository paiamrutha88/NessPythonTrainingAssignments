import json

employees = []
with open("data.txt","r") as File:
    lines = File.readlines()

headers = lines[0].strip().split(",")

for line in lines[1:]:
    values=line.strip().split(",")
    emp_dict = {
        "empid" : values[0],
        "empname": values[1],
        "emplocation": values[2],
        "empsalary": float(values[3])
    }
    employees.append(emp_dict)

result  ={"employees" : employees}
print(json.dumps(result, indent=2))