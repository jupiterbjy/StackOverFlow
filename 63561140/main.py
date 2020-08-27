from functools import wraps


def state_deco(func_main):
    """
    Decorator that mimics singledispatch for ease of interaction expansions.
    """

    # assuming no args are needed for interaction functions.
    func_main.dispatch_list = {}  # collect decorated functions

    @wraps(func_main)
    def wrapper(target):
        # dispatch target to destination interaction function.
        nonlocal func_main
        try:
            # find and run callable for target
            return func_main.dispatch_list[type(target)]()
        except KeyError:
            # If no matching case found, main decorated function will run instead.
            func_main()

    def register(target):
        # A decorator that register decorated function to main decorated function.
        def decorate(func_sub):
            nonlocal func_main
            func_main.dispatch_list[target] = func_sub

            def register_wrapper(*args, **kwargs):
                return func_sub(*args, **kwargs)

            return register_wrapper
        return decorate

    wrapper.register = register
    return wrapper


# Abstract class of reactions
class StateBase:
    # Implement per states
    def interaction(self, target) -> str:
        raise NotImplementedError


class StateA(StateBase):
    def interaction(self, target):
        # if interaction target is not registered, general() will run instead.

        @state_deco
        def general():
            # Add some necessary setups like os.chdir here, and below functions.
            # return is not needed, just for demonstration.
            return "A's reaction to undefined others."

        @general.register(StateA)
        def _():
            # Function name is not required, up to you whether name it or not.
            return "A's reaction of another A"

        @general.register(StateB)
        def _():
            return "A's reaction of B"

        return general(target)


class StateB(StateBase):
    def interaction(self, target):

        @state_deco
        def general():
            return "B's reaction to undefined others."

        @general.register(StateA)
        def _():
            return "B's reaction of A"

        @general.register(StateB)
        def _():
            return "B's reaction of another B"

        return general(target)

# Expand States responses further for more interactions choices.


if __name__ == '__main__':
    # pretending users got their roles via get_roles_single()
    user_A = StateA()
    user_B = StateB()

    print(f"interaction of A -> B:  {user_A.interaction(user_B)}")
    print(f"interaction of B -> A:  {user_B.interaction(user_A)}")
    print(f"interaction of A -> A:  {user_A.interaction(user_A)}")
    print(f"interaction of B -> B:  {user_B.interaction(user_B)}")
