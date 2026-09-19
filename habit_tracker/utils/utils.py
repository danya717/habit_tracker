from habit_tracker.utils.decorators import call_counter

@call_counter
def say_hi(name):
    return f'hi {name}'