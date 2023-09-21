auta = {
    "BMW": 2000,
    "Audi": 1666,
    "Mercedes": 5555,
    "Ford": 5536,
    "Porsche": 5885,
    "Ferrari": 7895,
    "Lamborghini": 1999,
}

for model, rok in auta.items():
    print(f"model: {model}, rok výroby: {rok}")




delka = len(auta)
print(f"{delka}")


auta["BMW"] = 2022
auta["Audi"] = 2023


for model, rok in auta.items():
    print(f"model: {model}, rok výroby: {rok}")