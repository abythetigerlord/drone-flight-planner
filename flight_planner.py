"""Estimate basic drone flight performance."""


def estimate_flight(battery_mah, voltage, average_current_a, cruise_speed_mps,
                    reserve_percent=25):
    """Return flight estimates using simple battery and speed assumptions."""
    if min(battery_mah, voltage, average_current_a, cruise_speed_mps) <= 0:
        raise ValueError("Battery, voltage, current, and speed must be positive.")
    if not 0 <= reserve_percent < 100:
        raise ValueError("Reserve must be between 0 and 99 percent.")

    usable_ah = battery_mah / 1000 * (1 - reserve_percent / 100)
    flight_hours = usable_ah / average_current_a
    flight_minutes = flight_hours * 60
    range_km = flight_hours * cruise_speed_mps * 3.6
    energy_wh = battery_mah / 1000 * voltage
    return {
        "energy_wh": energy_wh,
        "flight_minutes": flight_minutes,
        "range_km": range_km,
        "reserve_percent": reserve_percent,
    }


def main():
    print("Drone Flight Planner")
    battery = float(input("Battery capacity (mAh): "))
    voltage = float(input("Battery voltage (V): "))
    current = float(input("Average current (A): "))
    speed = float(input("Cruise speed (m/s): "))
    reserve = float(input("Battery reserve (%): "))
    result = estimate_flight(battery, voltage, current, speed, reserve)
    print(f"\nBattery energy: {result['energy_wh']:.1f} Wh")
    print(f"Estimated usable flight time: {result['flight_minutes']:.1f} minutes")
    print(f"Estimated one-way range: {result['range_km']:.2f} km")
    print(f"Planned reserve: {result['reserve_percent']:.0f}%")


if __name__ == "__main__":
    main()

