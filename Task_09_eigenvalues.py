"""Task 09: Eigenvector centrality in a small campus Wi-Fi network."""
import numpy as np

# Undirected links between four access points.
adjacency = np.array([[0., 1., 1., 0.],
                      [1., 0., 1., 1.],
                      [1., 1., 0., 1.],
                      [0., 1., 1., 0.]])
values, vectors = np.linalg.eig(adjacency)
idx = int(np.argmax(values.real))
dominant_value = float(values[idx].real)
importance = np.abs(vectors[:, idx].real)
importance /= importance.sum()

print(f"Dominant eigenvalue: {dominant_value:.4f}")
for label, score in zip(["Library", "Lab", "Lecture Hall", "Hostel"], importance):
    print(f"{label:15s}: {score:.4f}")
print("Eigenvector equation residual:",
      np.linalg.norm(adjacency @ vectors[:, idx] - values[idx] * vectors[:, idx]))

# Parameter experiment: add a link between Library and Hostel.
changed = adjacency.copy()
changed[0, 3] = changed[3, 0] = 1
new_values, new_vectors = np.linalg.eig(changed)
new_idx = int(np.argmax(new_values.real))
new_scores = np.abs(new_vectors[:, new_idx].real)
new_scores /= new_scores.sum()
print("Importance after adding Library-Hostel link:", np.round(new_scores, 4))
print("Interpretation: a node can gain importance when it connects to already "
      "well-connected parts of the network.")
