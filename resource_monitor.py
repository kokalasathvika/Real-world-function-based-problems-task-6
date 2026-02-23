def classroom_resource_monitor(resource_usage):
    overused = []

    for resource, hours in resource_usage.items():
        if hours > 8:   # Threshold for overuse
            overused.append(resource)

    if overused:
        print("Overused Resources:", ", ".join(overused))
        print("Energy Alert: Yes")
    else:
        print("Overused Resources: None")
        print("Energy Alert: No")
        # Sample Run
resources = {
    "Projector": 6,
    "AC": 9,
    "Lights": 4
}

classroom_resource_monitor(resources)