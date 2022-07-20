"""
Write a program to solve a classic ancient Chinese puzzle: 

We count 35 heads and 94 legs among the chickens and rs in a farm. 
How many rs and how many chickens do we have?

"""

def farm_animals(heads:int=35, legs:int=94):
    for r in range(1,heads+1):
        c = heads - r
        if ((2 * c) + (4 * r)) == legs:
            return c, r

chickens, rabbits = farm_animals()
print(f'Number of chickens: {chickens} and rabbits: {rabbits}')
print(f'Number of heads: {chickens + rabbits} and legs: {2 * chickens + 4 * rabbits}')



