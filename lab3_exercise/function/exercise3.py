def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (chickens * 2 + rabbits * 4) == numlegs:
            return chickens, rabbits
    return None, None

numheads = 35
numlegs = 94
chickens, rabbits = solve(numheads, numlegs)
if chickens is not None and rabbits is not None:
    print(f"Число кур: {chickens}, Число кроликов: {rabbits}")
else:
    print("Нет решения")