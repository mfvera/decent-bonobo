from typing import List
from itertools import pairwise

class Solution:
    def carFleet(self, target: int, positions: List[int], speeds: List[int]) -> int:
        self.target = target
        # Size O(n); Time O(n)
        vels = { position: vel for (position, vel) in zip(positions, speeds)}

        # Size O(n); Time O(nlog(n))
        # Order positions such that lead car is listed first.
        positions_sorted = list(reversed(sorted(positions)))

        # Size O(1); Time is ideally O(1) lol
        # There are at most n fleets, but we'll likely trim that back as we go.
        fleets = len(positions)

        # O(n) repetitions with O(1) content -> O(n)
        for leader, follower in pairwise(positions_sorted):
            vel_leader = vels[leader]
            vel_follower = vels[follower]
            # Cars meet -> decrement fleets, lower speed of current car to match the fleet.
            if self.cars_intersect_before_target(leader, vel_leader, follower, vel_follower):
                fleets -= 1
                vels[follower] = self.average_velocity_of_follower(leader, vel_leader, follower, vel_follower)
        
        # Overall Space: O(n); Time: O(nlog(n))
        return fleets

    # O(1) time and space
    def cars_intersect_before_target(self, start_leader: int, vel_leader: int, start_follower: int, vel_follower: int) -> float:
        time_to_target_leader = (self.target - start_leader) / vel_leader
        time_to_target_follower = (self.target - start_follower) / vel_follower
        return time_to_target_follower <= time_to_target_leader
    
    # O(1) time and space
    def average_velocity_of_follower(self, start_leader: int, vel_leader: int, start_follower: int, vel_follower: int) -> float:
        intersect_time = (start_follower - start_leader) / (vel_leader - vel_follower)
        distance_before_intersect = intersect_time * vel_follower
        time_to_target_after_intersect = (self.target - distance_before_intersect - start_follower) / vel_leader
        average = (self.target - start_follower) / (intersect_time + time_to_target_after_intersect)
        return average


"""
Initial Theorycrafting:
For each car, starting with the car out front:
    If preceding car catches up before end:
        decrement fleet count
        update speed of preceding car with the slower speed.
"""