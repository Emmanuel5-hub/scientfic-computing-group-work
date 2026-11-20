"""Task 05: Matrix transformations for a robot-floor coordinate map."""
import numpy as np

points = np.array([[0., 0.], [2., 0.], [2., 2.], [0., 2.]])
angle_degrees = 30.0
scale_x, scale_y = 1.5, 0.8
translation = np.array([3.0, 1.0])

angle = np.deg2rad(angle_degrees)
rotation = np.array([[np.cos(angle), -np.sin(angle)],
                    [np.sin(angle),  np.cos(angle)]])
scaling = np.diag([scale_x, scale_y])
linear_transform = rotation @ scaling
mapped_points = points @ linear_transform.T + translation

print("Original coordinates (m):\n", points)
print("Mapped coordinates (m):\n", np.round(mapped_points, 3))
print(f"Area scale factor (determinant): {np.linalg.det(linear_transform):.3f}")
print("Distances from origin after mapping:",
      np.round(np.linalg.norm(mapped_points, axis=1), 3))

alternative_transform = rotation @ np.diag([2 * scale_x, scale_y])
print("Area factor after doubling horizontal scale:",
      f"{np.linalg.det(alternative_transform):.3f}")
print("Interpretation: rotation changes orientation, scaling changes dimensions, "
      "and translation shifts every mapped point without changing area.")
