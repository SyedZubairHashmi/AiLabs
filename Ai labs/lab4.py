class VacuumAgent:
    def __init__(self, environment):
        self.environment = environment
        self.current_room = 0  # Starting room index

    def clean_room(self):
        if self.environment[self.current_room] == 'dirty':
            print(f"Cleaning room {self.current_room}")
            self.environment[self.current_room] = 'clean'
            return 25  # Reward for cleaning
        else:
            print(f"Room {self.current_room} is already clean")
            return -10  # Penalty for entering a clean room

    def move_to_next_room(self):
        self.current_room = (self.current_room + 1) % len(self.environment)
        print(f"Moving to room {self.current_room}")
        return -1  # Penalty for moving to a different room

# Example usage:
environment = ['dirty', 'clean', 'dirty']  # Example environment with 3 rooms
agent = VacuumAgent(environment)

for _ in range(5):  # Perform actions for 5 time steps
    score = agent.clean_room() + agent.move_to_next_room()
    print(f"Score: {score}")
