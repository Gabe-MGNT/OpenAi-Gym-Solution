# Acrobot DeepQ Learning 🎪🤖

Here is a solution using simple DeepQ Learning with replay memory to solve the acrobot task.


## Context
These types of task are now easy if you have already made the pendulum and cart pole. Once again, to solve this task efficiently we will have to use DeepQ Learning, here is such a solution.

## Training time
Nearly 1 hours 20 minutes (stopped at 172 episodes) (GPU : no GPU - CPU : Intel i7 10th gen)


## Trained weights
If you don't have time, and simply want to try the experience, I put the weights I got after training in a subfolder. 
Note : these weights are far from perfect and are not the best, but are enough to achieve the task or to see the result.

## Result
With a learning rate of 0.01, discount of 0.99, epsilon of 1.0, max steps of 500, 400 episodes, and a batch size of 256, here are the results : 

| Random case 1 | Random case 2 | Random case 3 |
|------------|------------|------------|
| ![Alt Text](img/AcrobotDQN7.gif) | ![Alt Text](img/AcrobotDQN8.gif) | ![Alt Text](img/AcrobotDQN9.gif) |