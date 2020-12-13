# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
amount = 30
denominations = [25, 10, 5, 1]
variations = {25: "quarters", 10: "dimes", 5 : "nickels", 1 : "pennies"}

def displayCombos(remaining, i, comb, flag):
    if flag: comb.append(flag)
    if remaining == 0 or (i+1) == len(denominations):
        if (i+1) == len(denominations) and remaining > 0:
           if remaining % denominations[i]:
               return 0
           comb.append( (remaining/denominations[i], denominations[i]) )
           i += 1
        while i < len(denominations):
            comb.append( (0, denominations[i]) )
            i += 1
        print(amount,"cents ="," + ".join("%d %s" % (n,variations[c]) for (n,c) in comb))
        return 1
    cur = denominations[i]
    return sum(displayCombos(remaining-x*cur, i+1, comb[:], (x,cur)) for x in range(0, int(remaining/cur)+1))

displayCombos(amount, 0, [], None)