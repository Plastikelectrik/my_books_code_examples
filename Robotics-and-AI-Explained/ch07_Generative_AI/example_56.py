# Retrieve the most relevant help text for a question
from sklearn.feature_extraction import text as fx
from sklearn.metrics.pairwise import cosine_similarity

manual = [
    "To charge the robot, drive it onto the dock.",
    "If the lidar is dirty, clean it with a soft cloth.",
    "Press the red button to stop the robot at once.",
    "Update the map after moving furniture.",
    "Replace the brush every three months.",
]
questions = ["how do I stop it in an emergency",
             "the robot is lost after moving the sofa",
             "battery is empty what do I do"]

vec = fx.TfidfVectorizer(stop_words="english")
M = vec.fit_transform(manual)
for q in questions:
    sims = cosine_similarity(vec.transform([q]), M)[0]
    best = sims.argmax()
    print(f"Q: {q}  (score {sims[best]:.2f})")
    print("   ->", manual[best])
