
def room_light_agent(percept):
    if percept == "Dark":
        return "Turn Light ON"
    elif percept == "Dim":
        return "Leave Light As Is"
    else:
        return "Turn Light OFF"

percept_sequence = ["Dark", "Dim", "Bright", "Dark"]

print("Percept\t\tAction")

for percept in percept_sequence:
    action = room_light_agent(percept)
    print(f"{percept}\t\t{action}")
