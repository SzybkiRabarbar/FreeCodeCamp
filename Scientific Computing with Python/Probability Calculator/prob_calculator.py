import copy
import random
#// Consider using the modules imported above.
from collections import Counter

class Hat:
    
    def __init__(self, **kwargs: dict[str, int]) -> None:
        self.contents = []
        for color, number in kwargs.items():
            [self.contents.append(color) for _ in range(number)]

    def draw(self, num_balls: int) -> list[str]:
        if num_balls >= len(self.contents):
            return self.contents
        balls_drawn = random.sample(self.contents, k=num_balls)
        for ball in balls_drawn:
            self.contents.pop(self.contents.index(ball))
        return balls_drawn
    
def experiment(hat: "Hat", expected_balls: dict[str, int], num_balls_drawn: int, num_experiments: int) -> float:
    m = 0
    for _ in range(num_experiments):
        copy_hat = copy.deepcopy(hat)
        list_balls_drawn = copy_hat.draw(num_balls_drawn)
        ball_counts = dict(Counter(list_balls_drawn))
        valid_counter = 0
        for color, number in ball_counts.items():
            if color in expected_balls.keys() and number >= expected_balls[color]:
                valid_counter+=1
        if valid_counter == len(expected_balls.keys()):
            m+=1
    return m / num_experiments

if __name__=="__main__":
    tophat = Hat(blue=4, red=2, green=6)
    probability = experiment(hat=tophat,expected_balls={"blue": 2,"red": 1},num_balls_drawn=4,num_experiments=3000)
    print(probability)
    