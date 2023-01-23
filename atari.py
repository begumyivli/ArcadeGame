
x = int(input())
y = int(input())
g = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
main_list =[]
begum=True
control=0
for i in range(x):
    list_ast = []
    for j in range(y):
        list_ast.append("*")
    main_list.append(list_ast)

for i in range(g):
    list_space = []
    for j in range(y):
        list_space.append(" ")
    main_list.append(list_space)

if x>0:
    for i in main_list:
        for j in i:
            print(j, end="")
        print()

list_ship=[" "]*y
if y%2 == 0:
    position= y//2-1
else:
    position= y//2
list_ship[position]="@"

if x>0:
    for k in list_ship:
        print(k, end="")
    print()
    print("-" * 72)

time=0
while(True):
    if "*" not in main_list[control]:
        print("YOU WON!")
        for i in main_list:
            for j in i:
                print(j, end="")
            print()
        for k in list_ship:
            print(k, end="")
        print()
        print("-" * 72)
        break
    act = input("Choose your action!\n")
    action = act.lower()
    if action == "exit":
        for i in main_list:
            for j in i:
                print(j, end="")
            print()
        for k in list_ship:
            print(k, end="")
        print()
        print("-" * 72)
        break
    time += 1

    if action == "left":
        list_ship=[" "]*y
        if position > 0:
            position -= 1
        else:
            pass
        list_ship[position] = "@"

    elif action == "right":
        list_ship=[" "]*y
        if position < y-1:
            position += 1
        else:
            pass
        list_ship[position] = "@"

    elif action == "fire":
        x_bullet=position
        y_bullet=(x+g-1)

        while y_bullet>=0:

            if main_list[y_bullet][x_bullet] == "*":
                main_list[y_bullet][x_bullet] = " "
                break

            else:
                main_list[y_bullet][x_bullet] = "|"

            for i in main_list:
                for j in i:
                    print(j, end="")
                print()
            for k in list_ship:
                print(k, end="")
            print()
            print("-" * 72)

            main_list[y_bullet][x_bullet] = " "
            y_bullet -= 1
    if "*" not in main_list[control]:
        print("YOU WON!")
        for i in main_list:
            for j in i:
                print(j, end="")
            print()
        for k in list_ship:
            print(k, end="")
        print()
        print("-" * 72)
        break


    if time % 5 == 0:
        if "*" in main_list[-1]:
            print("GAME OVER")
            for i in main_list:
                for j in i:
                    print(j, end="")
                print()
            for k in list_ship:
                print(k, end="")
            print()
            print("-" * 72)
            break
        for k in range(x + g - 1):
            main_list[x + g - 1 - k] = main_list[x + g - 2 - k]
        list_upspace = []
        for i in range(y):
            list_upspace.append(" ")
        main_list[0] = list_upspace
        control += 1

    for i in main_list:
        for j in i:
            print(j, end="")
        print()
    for k in list_ship:
        print(k, end="")
    print()
    print("-" * 72)


astr = 0
for a in main_list:
    astr = astr + a.count("*")
print("YOUR SCORE:", str(x*y-astr))

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

