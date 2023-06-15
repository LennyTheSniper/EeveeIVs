# Eevee Base Stats
eevee_base_stats = {
    "HP": 55,
    "Attack": 55,
    "Defense": 50,
    "Special Attack": 45,
    "Special Defense": 65,
    "Speed": 55
}

# Eeveelution Base Stats
eeveelution_base_stats = {
    "Vaporeon": [130, 65, 60, 110, 95, 65],
    "Jolteon": [65, 65, 60, 110, 95, 130],
    "Flareon": [65, 130, 60, 95, 110, 65],
    "Espeon": [65, 65, 60, 130, 95, 110],
    "Umbreon": [95, 65, 110, 60, 130, 65],
    "Leafeon": [65, 110, 130, 60, 65, 95],
    "Glaceon": [65, 60, 110, 130, 95, 65],
    "Sylveon": [95, 65, 65, 110, 130, 60]
}

def determine_eeveelution(ivs):
    relative_stats = {}
    for eeveelution, base_stats in eeveelution_base_stats.items():
        relative_stats[eeveelution] = sum([
            (ivs[stat] - base_stats[i]) ** 2 for i, stat in enumerate(eevee_base_stats)
        ])
    ranked_eeveelutions = sorted(relative_stats, key=relative_stats.get)
    return ranked_eeveelutions

# Prompt the user to enter IV values for the Eevee
ivs = {}
print("Please enter the IV values for the Eevee:")
for stat in eevee_base_stats:
    iv = int(input(f"{stat} IV: "))
    ivs[stat] = iv

ranked_eeveelutions = determine_eeveelution(ivs)
print("Ranking of Eeveelutions based on the given IVs:")
for rank, eeveelution in enumerate(ranked_eeveelutions, start=1):
    print(f"{rank}. {eeveelution}")