def server_load_classifier(cpu_readings):
    average_cpu = sum(cpu_readings) / len(cpu_readings)

    print("Average CPU Load:", round(average_cpu), "%")

    if average_cpu < 50:
        print("Server Status: Normal")
    elif 50 <= average_cpu <= 80:
        print("Server Status: Warning")
    else:
        print("Server Status: Critical")
        # Sample Run
server_load_classifier([45, 60, 70, 85, 90])