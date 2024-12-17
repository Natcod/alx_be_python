# noun = input("Enter a noun: ")
# verb = input("Enter a verb:")
# adjective = input("Enter an adjective: ")
# place = input("Enter a place: ")
# emotion =input("Enter an Emotion (e.g. happy, sad, angry): ")

# if place.lower() == "school":
#     place_description = "a beautiful class room with a beautiful class mate along side"
# elif place.lower() == "forest":
#     place_description = "a dark and mysterious forest filled with all trees."
# elif place.lower() == "beach":
#     place_description = "a sunny beach with golden sand and clear buew waves."
# else:
#     place_description = f"the wonder {place}."

# if emotion.lower() == "happy":
#     emotion_effect = "with a bign smile on its face"
# elif emotion.lower() == "sad":
#     emotion_effect = "with tears rolling down its cheeks"
# else:
#     emotion_effect = "with a look of determination"

# story = (f"Once upon a time, a {adjective} {noun} decided to {verb} in {place_description} "
#          f"It was feeling {emotion} that day, {emotion_effect}")

# print("\nHere's your Mad Libs story!")
# print(story)

adjective1 = input("Enter the first adjective: ")
adjective2= input("Enter the 2nd adjective: ")
adjective3= input("Enter the 3rd adjective: ")
adjective4= input("Enter the last adjective: ")

if adjective1.lower() == "sunny":
    adjective1_description = "a bright and sunny"
elif adjective1.lower() == "rainy":
    adjective1_description = "a dark and rainy"
else:
    adjective1_description = f"{adjective1}"

if adjective2.lower() == "little":
    adjective2_description = "a tiny little"
elif adjective2.lower() == "big":
    adjective2_description = "a naked gigantic big"
else:
    adjective2_description = f"{adjective2}"

if adjective3.lower() in ["starved", "hungry", "starving"]:
    adjective3_description = "starving to death"
elif adjective3.lower() in ["full", "satisfied", "happy"]:
    adjective3_description = "full and satisfied"
else:
    adjective3_description = f"{adjective3}"

if adjective4.lower() in ["unexpected", "surprising", "shocking"]:
    adjective4_description = "unexpected"

story = (f"On a beautiful {adjective1_description} day, I went to the zoo. "
         f"I saw a funny {adjective2_description} monkey swinging from the trees. "
         f"Then, I spotted a majestic {adjective3_description} lion lounging in the sun.  "
         f"What a wild and {adjective4_description} experience!")

print("\nHere's your Mad Libs story!")
print("\n", story)