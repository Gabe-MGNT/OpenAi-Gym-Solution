# Cart Pole (Simple DeepQ Learning with Replay Memory) 🛒🚩🤖


## Context
This task requires to balance a pole attached to cart that can only go left or right, the longer the pole is balanced the better it is.


## The simple DeepQ Learning solution (with Replay Memory)
This specific solution tried to implement a unique DeepQ Learning algorithm, using a replay memory for its training.
The neural network is used to approxiamte QValues in an envrionnment where the number of states is uncountable.


## Training time
Nearly 4 hours (GPU : no GPU - CPU : Intel i7 10th gen)


## Trained weights
If you don't have time, and simply want to try the experience, I put the weights I got after training in a subfolder. 
Note : these weights are far from perfect and are not the best, but are enough to achieve the task or to see the result.


## Result
With a learning rate of 0.01, discount of 0.99, epsilon of 1.0, max steps of 1000, 400 episodes, and a batch size of 128, here are the results : 

| Random case 1 | Random case 2 | Random case 3 |
|------------|------------|------------|
| ![Alt Text](img/PendulumDQN2.gif) | ![Alt Text](img/PendulumDQN3.gif) | ![Alt Text](img/PendulumDQN4.gif) |
