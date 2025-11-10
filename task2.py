class VacuumAgent:
    def __init__(self):
        self.percept_sequence = []
        self.action_table = {
            ('A', 'Dirty'): 'Suck',
            ('A', 'Clean'): 'Right',
            ('B', 'Dirty'): 'Suck',
            ('B', 'Clean'): 'Left',
        }
        self.current_location = 'A'
        self.percept = 'Dirty'

    def perceive(self, location, status):
        self.current_location = location
        self.percept = status
        self.percept_sequence.append((location, status))

    def get_action(self):
        return self.action_table.get((self.current_location, self.percept), 'Finish')

    def clean(self, steps=10):
        for _ in range(steps):
            action = self.get_action()
            print("Agent returns action:", action)
            if action == 'Finish':
                break
            print("Agent performs action:", action)
            if action == 'Suck':
                print("Vacuuming at location", self.current_location)
                self.percept = 'Clean'
            elif action == 'Right':
                print("Moving to the right")
                self.current_location = 'B'
            elif action == 'Left':
                print("Moving to the left")
                self.current_location = 'A'

def reflex_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    elif location == "B":
        return "Left"

def vacuum_cleaner():
    location = input("Enter the current location (A or B): ").strip().upper()
    status = input("Enter the status (Dirty or Clean): ").strip().capitalize()
    action = reflex_agent(location, status)
    print("Action:", action)

if __name__ == "__main__":
    agent = VacuumAgent()
    agent.perceive('A', 'Dirty')
    agent.perceive('B', 'Dirty')
    agent.clean()
    # interactive:
    # vacuum_cleaner()
