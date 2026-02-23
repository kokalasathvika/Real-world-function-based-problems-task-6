def seat_occupancy(total_seats, booked_seats):
    booked_count = len(booked_seats)
    occupancy = (booked_count / total_seats) * 100

    print("Occupancy:", round(occupancy), "%")

    if occupancy == 100:
        print("Show Status: Housefull")
    elif occupancy >= 75:
        print("Show Status: Almost Full")
    else:
        print("Show Status: Seats Available")
        # Sample Run (150 bookings)
seat_occupancy(200, [1]*150)