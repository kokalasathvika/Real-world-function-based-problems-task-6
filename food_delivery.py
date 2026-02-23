def estimate_delivery_time(distance, traffic, weather):
    base_time = distance * 5  # 5 minutes per km

    # Traffic delay
    if traffic.lower() == "high":
        base_time += 15
    elif traffic.lower() == "medium":
        base_time += 10
    elif traffic.lower() == "low":
        base_time += 5

    # Weather delay
    if weather.lower() == "rainy":
        base_time += 10
    elif weather.lower() == "stormy":
        base_time += 20

    print("Estimated Delivery Time:", base_time, "minutes")


# Sample Run
estimate_delivery_time(8, "High", "Rainy")