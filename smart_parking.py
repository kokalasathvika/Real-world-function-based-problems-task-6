def smart_parking_system(capacity, vehicle_logs):
    current_parked = 0
    peak_usage = 0

    for log in vehicle_logs:
        if log == "IN":
            current_parked += 1
        elif log == "OUT" and current_parked > 0:
            current_parked -= 1

        # Track peak usage
        if current_parked > peak_usage:
            peak_usage = current_parked

    print("Currently Parked Vehicles:", current_parked)
    print("Peak Parking Usage:", peak_usage)

    if current_parked > capacity:
        print("Parking Status: Exceeded Capacity 🚨")
    else:
        print("Parking Status: Available")


# Sample Run
smart_parking_system(50, ["IN", "IN", "IN", "OUT", "IN", "IN", "OUT"])