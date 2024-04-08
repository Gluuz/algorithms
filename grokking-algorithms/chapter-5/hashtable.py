# Initialize an empty dictionary to simulate a hashtable
voted = {}

# Function to check if a voter has already voted
def check_voter(name):
    # Check if the voter's name exists in the voted dictionary
    if voted.get(name):
        # If the voter's name exists, print a message to "kick them out!"
        print("kick them out!")
    else:
        # If the voter's name doesn't exist, 
        # mark them as voted and print a message to "let them vote!"
        voted[name] = True
        print("let them vote!")