def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

grams = float(input())
print(f"{grams} грамм(а) = {grams_to_ounces(grams):.2f} унции")
