# Frozen Lake QLearning 🏔️🥶🤖

Here is a solution using QLearning to solve the Frozen Lake task.

## Context
The task here is to bring a christmas elf to a gift by avoiding the holes on the ground. That is a perfect task for QLearning, but still depends on...

## The slippery factor
This task has kind of 2 versions, depending on whether you set is_slippery to True or False. If it's set to True, then after each action taken (move) there is a probability of 33% to move in the intended direction, otherwise it will move in an other direction.

This factor changes everything, because it makes the situation way more random than it used to be, and make the algorithm struggle to converge.

As a result, I will try to solve the 2 situations.
