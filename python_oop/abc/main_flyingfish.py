#!/usr/bin/env python3
"""Test Task 2: FlyingFish (multiple inheritance)."""
from flyingfish import Fish, FlyingFish

flying_fish = FlyingFish()
flying_fish.swim()
flying_fish.fly()
flying_fish.habitat()

print(FlyingFish.mro())
