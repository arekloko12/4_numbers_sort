a = int(input("Enter the 1-st number "))
b = int(input("Enter the 2-nd number "))
c = int(input("Enter the 3-td number "))
d = int(input("Enter the 4-th number "))

table_of_numbers = []


if a >= b:
    if a >= c:
        if a >= d:
            table_of_numbers.append(str(a)+"(a)")
            if b >= c:
                if b >= d:
                    table_of_numbers.append(str(b)+"(b)")
                    if c >= d:
                        table_of_numbers.append(str(c)+"(c)")
                        table_of_numbers.append(str(d)+"(d)")
                    else:
                        table_of_numbers.append(str(d)+"(d)")
                        table_of_numbers.append(str(c)+"(c)")
                else:
                    table_of_numbers.append(str(d)+"(d)")
                    table_of_numbers.append(str(b)+"(b)")
                    table_of_numbers.append(str(c)+"(c)")
            else:
                if b >= d:
                    if c >= d:
                        table_of_numbers.append(str(c)+"(c)")
                        table_of_numbers.append(str(b)+"(b)")
                        table_of_numbers.append(str(d)+"(d)")
                else:
                    if c >= d:
                        table_of_numbers.append(str(c)+"(c)")
                        table_of_numbers.append(str(d)+"(d)")
                        table_of_numbers.append(str(b)+"(b)")
                    else:
                        table_of_numbers.append(str(d)+"(d)")
                        table_of_numbers.append(str(c)+"(c)")
                        table_of_numbers.append(str(b)+"(c)")
        else:
            if b >= c:
                a = str(a)+"(a)"
                b = str(b)+"(b)"
                c = str(c)+"(c)"
                d = str(d)+"(d)"
                table_of_numbers = [d, a, b, c]
            else:
                a = str(a)+"(a)"
                b = str(b)+"(b)"
                c = str(c)+"(c)"
                d = str(d)+"(d)"
                table_of_numbers = [d, a, c, b]
    else:
        if a >= d:
            if b >= d:
                a = str(a)+"(a)"
                b = str(b)+"(b)"
                c = str(c)+"(c)"
                d = str(d)+"(d)"
                table_of_numbers = [c, a, b, d]
            else:
                a = str(a)+"(a)"
                b = str(b)+"(b)"
                c = str(c)+"(c)"
                d = str(d)+"(d)"
                table_of_numbers = [c, a, d, b]
else:
    if a >= c:
        if a >= d:
            if c >= d:
                a = str(a)+"(a)"
                b = str(b)+"(b)"
                c = str(c)+"(c)"
                d = str(d)+"(d)"
                table_of_numbers = [b, a, c, d]
            else:
                a = str(a)+"(a)"
                b = str(b)+"(b)"
                c = str(c)+"(c)"
                d = str(d)+"(d)"
                table_of_numbers = [b, a, d, c]
        else:
            if b >= d:
                a = str(a)+"(a)"
                b = str(b)+"(b)"
                c = str(c)+"(c)"
                d = str(d)+"(d)"
                table_of_numbers = [b, d, a, c]
            else:
                a = str(a)+"(a)"
                b = str(b)+"(b)"
                c = str(c)+"(c)"
                d = str(d)+"(d)"
                table_of_numbers = [d, b, a, c]
    else:
        if a >= d:
            if b >= c:
                a = str(a)+"(a)"
                b = str(b)+"(b)"
                c = str(c)+"(c)"
                d = str(d)+"(d)"
                table_of_numbers = [b, c, a, d]
        else:
            if b >= c:
                if b >= d:
                    if c >= d:
                        a = str(a)+"(a)"
                        b = str(b)+"(b)"
                        c = str(c)+"(c)"
                        d = str(d)+"(d)"
                        table_of_numbers = [b, c, d, a]
                    else:
                        a = str(a)+"(a)"
                        b = str(b)+"(b)"
                        c = str(c)+"(c)"
                        d = str(d)+"(d)"
                        table_of_numbers = [b, d, c, a]
            else:
                if b >= d:
                    a = str(a)+"(a)"
                    b = str(b)+"(b)"
                    c = str(c)+"(c)"
                    d = str(d)+"(d)"
                    table_of_numbers = [c, b, d, a]
                else:
                    a = str(a)+"(a)"
                    b = str(b)+"(b)"
                    c = str(c)+"(c)"
                    d = str(d)+"(d)"
                    table_of_numbers = [c, d, b, a]

for i in range(4):
    print(table_of_numbers[i], end=", ")