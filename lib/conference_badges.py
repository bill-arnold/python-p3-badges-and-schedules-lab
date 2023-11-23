def badge_maker(name):
    """Create and return a badge message."""
    return f"Hello, my name is {name}."

def batch_badge_creator(speakers):
    """Generate a list of badge messages for a list of speakers."""
    return [badge_maker(speaker) for speaker in speakers]

def assign_rooms(speakers):
    """Assign each speaker to a room and return a list of room assignments."""
    # Using enumerate to get both the speaker and their index (room number)
    return [f"Hello, {speaker}! You'll be assigned to room {index + 1}!" for index, speaker in enumerate(speakers)]

def printer(speakers):
    """Print badge messages and room assignments for a list of speakers."""
    badges = batch_badge_creator(speakers)
    rooms = assign_rooms(speakers)

    for badge in badges:
        print(badge)

    for room_assignment in rooms:
        print(room_assignment)

# Example usage:
speakers_list = ["Arel", "Carol"]
printer(speakers_list)
