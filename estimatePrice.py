import unicodedata
import GradientDescent.Parser as Parser

def is_numeric(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    
    return False

theta = Parser.parse('./GradientDescent/variables.csv')
t0 = theta[0][0]
t1 = theta[1][0]

print("Enter a mileage:")
x = input()

if is_numeric(x) == False:
    print("Not a number")
    quit()

res = t0 + (t1 * (float(x) / 10000))

print("Your mileage is priced at", "{0:.2f}".format(res), "euros")    
