def find_last_man_with_gun(total_people):
    # Initialize a list to represent people in the circle
    people = list(range(1, total_people + 1))
    
    # Start the killing process
    current_person_index = 0
    while len(people) > 1:
        # The current person shoots the next person
        next_person_index = (current_person_index + 1) % len(people)
        del people[next_person_index]
        
        # Move to the person who received the gun
        current_person_index = (next_person_index) % len(people)
    
    # last person remaining
    return people[0]

total_people = 100

last_person = find_last_man_with_gun(total_people)
print("The last person remaining with the gun is:", last_person)
