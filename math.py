import random


def estimate_pi(num_samples):
    inside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        # Check if the point (x, y) is inside the unit circle
        if x ** 2 + y ** 2 <= 1:
            inside_circle += 1

    # Estimate pi based on the ratio of points inside the circle to total points
    estimated_pi = (inside_circle / num_samples) * 4

    return estimated_pi


num_samples = 1000000  # You can adjust the number of samples for better accuracy
pi_estimate = estimate_pi(num_samples)
print(f"Estimated Pi: {pi_estimate}")
