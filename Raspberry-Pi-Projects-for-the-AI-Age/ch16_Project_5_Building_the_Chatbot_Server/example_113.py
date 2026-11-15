import numpy as np

def normalize(m):
    m = np.asarray(m, dtype=np.float32)
    return m / np.linalg.norm(m, axis=-1, keepdims=True)

def top_k(query_vec, matrix, k=3, min_score=0.35):
    """Return (index, score) pairs of the best chunks."""
    scores = normalize(matrix) @ normalize(query_vec)
    order = np.argsort(scores)[::-1][:k]
    return [(int(i), float(scores[i])) for i in order
            if scores[i] >= min_score]

# Test with 4 invented 3-dimensional "embeddings"
chunks = ["router reset", "boiler service",
          "film library", "router password"]
matrix = [[0.9, 0.1, 0.0], [0.0, 0.2, 0.9],
          [0.1, 0.9, 0.1], [0.8, 0.0, 0.3]]
questions = {"router question": [1.0, 0.0, 0.1],
             "unrelated question": [-0.5, -0.5, 0.0]}
for name, q in questions.items():
    hits = top_k(q, matrix, k=2)
    print(name)
    for i, s in hits:
        print(f"   {chunks[i]:16s} score {s:.2f}")
    if not hits:
        print("   no good match")
