from collections import deque

def is_mango_seller(name):
    """Check if the name ends with 'm', indicating a mango seller."""
    return name[-1] == 'm'

# Defining the relationships in the graph
relationships = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}

def search_mango_seller(start_person):
    """Search for a mango seller starting from the given person."""
    # Initialize a queue for breadth-first search
    search_queue = deque()
    # Add the starting person to the queue
    search_queue += [start_person]
    # Keep track of people already searched
    searched = set()

    # Loop until the queue is empty
    while search_queue:
        person = search_queue.popleft()  # Get the next person from the queue

        # Check if this person has already been searched
        if person in searched:
            continue

        # Check if the person is a mango seller
        if is_mango_seller(person):
            print(person + " is a mango seller!")
            return True

        # Add this person's connections to the search queue
        search_queue += relationships[person]

        # Mark this person as searched
        searched.add(person)

    # If no mango seller is found after searching all connections
    print("No mango seller found.")
    return False

# Start the search from "you"
search_mango_seller("you")
