#! python3

PRICES={'MA100':1750, 'MA101':1850, 'MA102':2000}

import pyperclip
import sys

if len(sys.argv)<2:
    print("Usage : py pi.py [model_name] - copy model's price")
    sys.exit()

model = sys.argv[1]

if model in PRICES:
    pyperclip.copy(str(PRICES[model]))
    print("Model " + model + "'s prices, " + str(PRICES[model]) + " has been copied to clipboard.")
else:
    print("There is no price information for the " + model + ".")
