
def Prog1():
    print('Expense Application')
    expen = [2200,2350,2600,2130,2190]
    ex_diff = expen[1] - expen[0]
    print("{} was spent extra in feb.".format(ex_diff))

    total_exp_in_first_quater = GetTotalExpense([expen[0],expen[1],expen[2]])
    print("Total expenses in first quarter is {}".format(total_exp_in_first_quater))

    search_value = 2000
    isFound = False
    found_index =0

    for i in range(len(expen)):
        if expen[i] == search_value:
            isFound = True
            found_index = i+1
            break

    if isFound:
        print("{} was spent at month {}".format(search_value, found_index))
    else:
        print("{} was not spent at any month".format(search_value))

    expen.append(1980)
    expen[3] +=200

    total_exp = GetTotalExpense(expen)
    print("Total expenses is {}".format(total_exp))

def GetTotalExpense(list):
    total =0
    for i in range(len(list)):
        total += list[i]
    return total


if __name__ == "__main__":
    Prog1()
