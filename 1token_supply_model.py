# Simple Token Supply Growth Model
# Author: Michael (Token Engineering Learner)

initial_supply = 1_000_000      # starting supply
growth_rate = 0.05              # 5% yearly growth
years = 10                      # simulate for 10 years

supply = initial_supply
print("Year | Total Supply")
print("----------------------")

for year in range(1, years + 1):
    supply *= (1 + growth_rate)
    print(f"{year}    | {int(supply):,}")
