import gym
env = gym.make('MountainCar-v0', render_mode="human")

env.reset()
env.render()