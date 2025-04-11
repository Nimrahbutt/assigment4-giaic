C: int = 299_792_458  # The speed of light in m/s

def main():
    mass_in_kg: float = float(input("Enter mass in kilograms: "))

    # Calculate energy using E = mc^2
    energy_in_joules: float = mass_in_kg * (C ** 2)

    # Display results
    print("\ne = m * C^2...")
    print(f"m = {mass_in_kg} kg")
    print(f"C = {C} m/s")
    print(f"Energy = {energy_in_joules:,.2f} joules")

if __name__ == '__main__':
    main()

