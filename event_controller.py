def event_registration_controller(capacity, registrations):
    if registrations <= capacity:
        print("Confirmed Registrations:", registrations)
        print("Waitlisted Users: 0")
        print("Registration Status: Open")
    else:
        waitlist = registrations - capacity
        print("Confirmed Registrations:", capacity)
        print("Waitlisted Users:", waitlist)
        print("Registration Status: Closed")
        # Sample Run
event_registration_controller(100, 105)