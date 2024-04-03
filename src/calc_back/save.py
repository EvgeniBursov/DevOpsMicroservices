

class Originator:
    def __init__(self):
        self._state = None

    def set_state(self, state):
        print("Originator: Setting state to", state)
        self._state = state

    def save_to_memento(self):
        print("Originator: Saving to Memento.")
        return Memento(self._state)

    def restore_from_memento(self, memento):
        self._state = memento.get_state()
        print("Originator: State after restoring from Memento:", self._state)

class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

class Caretaker:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        print("Caretaker: Adding Memento.")
        self._mementos.append(memento)

    def get_memento(self, index):
        return self._mementos[index]

# Example usage:
originator = Originator()
caretaker = Caretaker()

originator.set_state("State 1")
memento1 = originator.save_to_memento()
caretaker.add_memento(memento1)

originator.set_state("State 2")
memento2 = originator.save_to_memento()
caretaker.add_memento(memento2)

originator.set_state("State 3")
memento3 = originator.save_to_memento()
caretaker.add_memento(memento3)

print("\nRestoring to State 1:")
originator.restore_from_memento(caretaker.get_memento(0))

print("\nRestoring to State 2:")
originator.restore_from_memento(caretaker.get_memento(1))

print("\nRestoring to State 3:")
originator.restore_from_memento(caretaker.get_memento(2))
