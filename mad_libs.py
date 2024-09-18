adjective_1 = input("what's the adjective: ")
adjective_2 = input("what's the adjective: ")
adjective_3 = input("what's the adjective: ")
adjective_4 = input("what's the adjective: ")

#creating a mad lib program
weather = "rainy", "sunny", "calm", "cloudy", "windy"
descriptive_noun = "looking","gloommy", "moody", "handsome", "fearce", "insightful", "jumping"

if adjective_1 == "weather":
    weather_comment = "pass"
else:
    weather_comment = "fail"
    
if adjective_2 and adjective_3 and adjective_4 == descriptive_noun:
    adjective_comment = "pass"
else:
    adjective_comment = "fail"

story = f"""
         On a beautiful {adjective_1} day,
         I went to the zoo. I saw a funny {adjective_2}
         monkey swinging from the trees. Then, spotted a majestic {adjective_3}
         lion lounging in the sun. What a wild and {adjective_4} experience!"""
print(story)