import math

def simulate_shot_put_throw(velocity, angle_deg):
    angle_rad = math.radians(angle_deg)
    g = 9.8  # m/s^2
    distance = (velocity ** 2) * math.sin(2 * angle_rad) / g

    print(f"Initial Velocity: {velocity} m/s")
    print(f"Angle of Release: {angle_deg} degrees")
    print(f"Estimated Throw Distance: {distance:.2f} meters\n")

if __name__ == "__main__":
    simulate_shot_put_throw(14, 45)
    simulate_shot_put_throw(15, 35)
    simulate_shot_put_throw(13, 50)
