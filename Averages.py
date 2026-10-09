values,mean = [],None

print("Enter the values, 'x' for an unknown value and '/' to stop entering values")
while True:
    Input = input("-> ").strip().lower()
    if Input == '/':
        break
    if Input == 'x':
        values.append('x')
    else:
        values.append(float(Input))

totalvals = sum(v for v in values if v != 'x') #total of all values in values but excludes "x"
if 'x' in values:
    print("Enter the mean")
    while True:
        Input = input("-> ").strip().lower()
        if Input=='x' or Input.replace(".","",1).isdigit(): #removes decimal point once so "3..4" is False
            mean = float(Input)
            break
    missing = mean*len(values) - totalvals
    values[values.index('x')] = missing
else:
    mean = totalvals/len(values)

print("The values are:")
for i, v in enumerate(values):#i gives index and v give the value at the index
    print(f"Value {i+1} = {v}")#i+1 so values start at 1
print(f"The mean is:\n{mean}")
