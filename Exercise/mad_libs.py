noun = input("Enter a noun: ")
verb = input("Enter a verb:")
adjective = input("Enter an adjective: ")
place = input("Enter a place: ")
emotion =input("Enter an Emotion (e.g. happy, sad, angry): ")

if place.lower() == "school":
    place_description = "a beautiful class room with a beautiful class mate along side"
elif place.lower() == "forest":
    place_description = "a dark and mysterious forest filled with all trees."
elif place.lower() == "beach":
    place_description = "a sunny beach with golden sand and clear buew waves."
else:
    place_description = f"the wonder {place}."

if emotion.lower() == "happy":
    emotion_effect = "with a bign smile on its face"
elif emotion.lower() == "sad":
    emotion_effect = "with tears rolling down its cheeks"
else:
    emotion_effect = "with a look of determination"

story = (f"Once upon a time, a {adjective} {noun} decided to {verb} in {place_description} "
         f"It was feeling {emotion} that day, {emotion_effect}")

print("\nHere's your Mad Libs story!")
print(story)