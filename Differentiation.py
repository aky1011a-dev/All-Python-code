def differentialprint(textbefore,textafter):
    for i in range(len(textbefore)):
        print(" ",end="")
    print(" dy")
    print(f"{textbefore} -- {textafter}")
    for i in range(len(textbefore)):
        print(" ",end="")
    print(" dx")
    
def equationinput(text):
    arr = []
    while True:
        valid,toreturn = True,""
        Input = input(text).strip().lower()
        Input = Input.replace("+", " + ").replace("-", " - ")
        fixed = ""
        i = 0
        while i < len(Input):
            if Input[i] == "x":
                fixed += "x"
                if i + 1 < len(Input) and Input[i + 1] != "^":
                    fixed += "^1"
                i += 1
            else:
                fixed += Input[i]
                i += 1
        Input = fixed

        
        arr = Input.split()
        combined = []
        i = 0
        while i < len(arr):
            if arr[i] in "+-":
                combined.append(arr[i] + arr[i+1])
                i += 2
            else:
                combined.append(arr[i])
                i += 1
        arr = combined
        arr = [term for term in arr if "x" in term]
        for i in range(len(arr)):
            temp = arr[i].replace("x","",1).replace("^","",1)
            for j in range(len(temp)):
                if not(temp[j] in "0123456789.-+"):
                    valid = False
        try:
            for i in range(len(arr)):
                newarr = ""
                if arr[i].endswith("x"):
                    arr[i]+="^1"
                if arr[i].startswith("x"):
                    arr[i] = "1"+arr[i]
                temp2 = arr[i].split("x")
                for j in range(len(temp2)):
                    temp2[j] = temp2[j].replace("^","")
                newarr += str(float(temp2[0])*float(temp2[1]))
                newarr += "x"
                newarr += str(float(temp2[1])-1.0)
                arr[i] = newarr
        except:
            print("test error")
        if not valid:
            print("Invalid Input")
        else:
            break
    clean_terms = []

    for term in arr:
        term = term.replace("x0", "")   # remove x^0 terms
        term = term.replace("x", "x^")
        clean_terms.append(term)
    toreturn = clean_terms[0]
    for term in clean_terms[1:]:
        if term.startswith("-"):
            toreturn += term
        else:
            toreturn += "+" + term

    toreturn = (toreturn
    .replace(".0","")
    .replace("x^0","")
    .replace("^^","^")
    .replace("x^1","x")
    .replace(" ",""))
    return toreturn


print("This gets the gradient (equation for a specific x coordinate)\nof an eqaution with only one y value for each x")
differentialprint("Represented by:","")
print("Use '^' to enter powers.")
while True:
    print("Enter the equation of the graph in terms of 'y'/'f(x)'")
    ans = equationinput("f(x) = ")
    differentialprint("The equation is:",f"= {ans}")
    endcode = input("Do you want to end code: y/other")
    if endcode.lower().strip() == 'y':
        break
    

