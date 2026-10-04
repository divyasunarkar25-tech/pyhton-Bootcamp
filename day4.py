vehicle_type = input("Enter vehicle type: ").lower()
fastag_active = input("Is FASTag active? (yes/no): ").lower() == "yes"
is_national_holiday = input("Is it a national holiday? (yes/no): ").lower() == "yes"

if not fastag_active:
    print("Double toll penalty applied: cash mode")

elif is_national_holiday:
    print("Festive waiver applied: half toll")

else:
    if vehicle_type == "car":
        print("Toll amount: 100 rupees")

    elif vehicle_type == "suv":
        print("Toll amount: 150 rupees")

    elif vehicle_type == "truck":
        print("Toll amount: 300 rupees")

    else:
        print("Invalid vehicle category")