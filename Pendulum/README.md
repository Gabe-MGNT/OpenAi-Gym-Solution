# Pendulum DeepQ Learning🕰️🤖

Here is a solution using simple DeepQ Learning with replay memory to solve the pendulum task.

## Context
These types od tasks begin to be quite complex, this task is very similar to the Cart Pole task. Once again, to solve it efficiently we will have to use DeepQ Learning, here is a solution.


## Training time
Nearly 4 hours (GPU : no GPU - CPU : Intel i7 10th gen)

The learning rate has a huge importance in training time, at the beginning I tried with a lr of 0.0025 and it didn't mangaed to convergence even after 4 hours. With a lr of 0.01, it was way faster to converge.


## Trained weights
If you don't have time, and simply want to try the experience, I put the weights I got after training in a subfolder. 
Note : these weights are far from perfect and are not the best, but are enough to achieve the task or to see the result.


## Result
With a learning rate of 0.01, discount of 0.99, epsilon of 1.0, max steps of 200, 400 episodes, and a batch size of 256, here are the results : 

| Random case 1 | Random case 2 | Random case 3 |
|------------|------------|------------|
| ![Alt Text](img/PendulumDQN2.gif) | ![Alt Text](img/PendulumDQN3.gif) | ![Alt Text](img/PendulumDQN4.gif) |