class ActionStack:
    def __init__(self):
        self.actions = []

    def execute(self):
        for action in self.actions:
            callback, args = action
            callback(*args)


class ActionStackBuilder:
    def __init__(self, action_stack):
        self.action_stack: ActionStack = action_stack

    def add(self, callback, *args):
        self.action_stack.actions.append((callback, args))
        return self

    def build(self):
        return self.action_stack


def build_action():
    return ActionStackBuilder(ActionStack())
