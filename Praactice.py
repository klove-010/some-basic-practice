

class DoSomething:

    def __init__(self, name):
        self.name = name
        self.actions= []

    def new_action(self, action):
        self.actions.append(action)
x = DoSomething('Ted')
print(x.name)
x.new_action('Fight')
x.new_action('Dance')
print(x.actions)
