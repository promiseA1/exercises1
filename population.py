current_population = 3120032486

birth_per_seconds = 7
death_per_seconds = 13
immigrants_per_seconds = 45

seconds_per_year = 365 * 24 * 60 * 60

birth_per_year = seconds_per_year // birth_per_seconds
death_per_year = seconds_per_year // death_per_seconds
immigrants_per_year = seconds_per_year // immigrants_per_seconds

net_population_change_per_year = birth_per_year - death_per_year + immigrants_per_year

for year in range(1 , 6):
    current_population += net_population_change_per_year 
    print(f"Year {year}: {current_population}")
