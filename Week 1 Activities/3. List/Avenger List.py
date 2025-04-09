justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
number_of_members = len(justice_league)
print(f"Initial Justice League: {justice_league}")
print(f"Number of members: {number_of_members}")

justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("\nAfter adding Batgirl and Nightwing:")
print(justice_league)

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("\nAfter making Wonder Woman the leader:")
print(justice_league)

justice_league.remove("Superman")
justice_league.insert(justice_league.index("Flash"), "Superman")
print("\nAfter moving Superman between Aquaman and Flash:")
print(justice_league)

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("\nNew Justice League:")
print(justice_league)

justice_league.sort()
new_leader = justice_league[0]
print("\nAfter sorting alphabetically:")
print(justice_league)
print(f"New leader: {new_leader}")
