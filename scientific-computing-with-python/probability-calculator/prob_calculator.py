import copy
import random
from typing import List


class Hat:
    """
    A class representing a hat that can be filled with balls
    Balls can then be drawn randomly from the hat
    """

    def __init__(self, **kwargs) -> None:
        self.contents = []
        for color, amount in kwargs.items():
            self.contents.extend([color for _ in range(amount)])

    def draw(self, amount: int) -> List[str]:
        """
        Draw `amount` balls randomly from the hat without replacement
        """
        balls = []
        for _ in range(amount):
            # No more balls in the hat
            if not self.contents:
                return balls

            index = random.randint(0, len(self.contents) - 1)
            balls.append(self.contents.pop(index))

        return balls


def experiment(hat: 'Hat', expected_balls: dict, num_balls_drawn: int, num_experiments: int) -> float:
    """
    Compute the probability of a draw experiment
    by doing the experiment `num_experiments` times
    and counting the number of success
    """
    success = 0

    for _ in range(num_experiments):
        # Make a copy so as not to alter the original hat during draw
        experience_hat = copy.deepcopy(hat)

        drawn_balls = experience_hat.draw(num_balls_drawn)

        # Check if we have drawn all of the expected balls
        for color in expected_balls.keys():
            if expected_balls[color] > drawn_balls.count(color):
                break
        else:
            success += 1

    return success / num_experiments
