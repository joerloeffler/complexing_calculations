def calculate_concentration(mg_per_ml, molar_mass):
    """
    Calculate the molarity (mol/l) from concentration in mg/ml and molar mass in g/mol.
    """
    return (mg_per_ml / 1000) / molar_mass  # Conversion to mol/l

def calculate_moles(concentration, volume_liters):
    """
    Calculate the moles based on concentration (mol/l) and volume (L).
    """
    return concentration * volume_liters

def calculate_volume_needed(moles, concentration):
    """
    Calculate the volume (in liters) needed to achieve a specific number of moles
    given a molarity.
    """
    return moles / concentration

def calculate_buffer_volume(total_volume, *compound_volumes):
    """
    Calculate the buffer volume needed by subtracting the sum of the compound volumes from the total volume.
    """
    return total_volume - sum(compound_volumes)

# Sample Input Data
proteins = {
    'AB': {'g_per_mol': 50000, 'mg_per_ml': 0.98, 'ratio': 4},
    'AG': {'g_per_mol': 180000, 'mg_per_ml': 4.0112, 'ratio': 1},
    'complex': {'g_per_mol': 330000, 'mg_per_ml': 0.7, 'ratio': 1},
}

# Final target values
final_complex_concentration = 0.7  # in mg/ml
final_complex_molecular_weight = 330000  # in g/mol
final_volume = 21e-6  # in L (21 µL)

# Calculate the final complex molarity
complex_concentration = calculate_concentration(final_complex_concentration, final_complex_molecular_weight)
moles_complex = calculate_moles(complex_concentration, final_volume)

# Calculate moles and volumes for each protein
compound_volumes = {}
for compound, data in proteins.items():
    # If it's not the complex, calculate the molarity
    if compound != 'complex':
        compound_concentration = calculate_concentration(data['mg_per_ml'], data['g_per_mol'])
        compound_moles = moles_complex * data['ratio']  # Adjust by ratio
        compound_volume = calculate_volume_needed(compound_moles, compound_concentration)
        compound_volumes[compound] = compound_volume

# Calculate the buffer volume
buffer_volume = calculate_buffer_volume(final_volume, *compound_volumes.values())

# Print the results
print("Results:")
for compound, volume in compound_volumes.items():
    print(f"{compound}: {volume * 1e6:.2f} µL")  # Convert L to µL
print(f"Buffer: {buffer_volume * 1e6:.2f} µL")  # Convert L to µL
