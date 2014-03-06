# Calculates and displays coin combination possibilities for exact change
# Example: 10 cents can be represented in four ways: a dime, two nickels, a nickel and five pennies, ten pennies
# Need to clean up the recursion bit, but it works for American currency

cents = 10
denominations = [25, 10, 5, 1]
change_drawer = {25: "quarter(s)", 10: "dime(s)", 5 : "nickel(s)", 1 : "pennies"}

def count_combos(coins, i, combo, add):
    if add: combo.append(add)
    if coins == 0 or (i+1) == len(denominations):
        if (i+1) == len(denominations) and coins > 0:
            combo.append( (coins, denominations[i]) )
            i += 1
        while i < len(denominations):
            combo.append( (0, denominations[i]) )
            i += 1
        print " ".join("%d %s" % (n,change_drawer[c]) for (n,c) in combo)
        return True
    cur = denominations[i]
    return sum(count_combos(coins-x*cur, i+1, combo[:], (x,cur)) for x in range(0, int(coins/cur)+1))

print('\n')
print count_combos(cents, 0, [], None)
