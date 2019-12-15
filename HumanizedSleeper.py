import time
from random import random

class HumanizedSleeper:

    def __init__(self,
        min_variance_scale,
        max_variance_scale,
        highest_sleep_variance_allowed):
            self.min_variance_scale = min_variance_scale
            self.max_variance_scale = max_variance_scale
            self.highest_sleep_variance_allowed = highest_sleep_variance_allowed

    def sleep_with_variance(self, seconds):
        min_variance = self.min_variance_scale * seconds
        max_variance = self.max_variance_scale * seconds
        variance = min_variance + (max_variance - min_variance) * random()
        variance = min(variance, self.highest_sleep_variance_allowed)
        seconds_with_variance = seconds + variance
        time.sleep(seconds_with_variance)