import numpy as np
import random
import matplotlib.pyplot as plt
from uiadaptationenv import UIAdaptationEnv

# Define the environment
env = UIAdaptationEnv()
observation_space_size = env.observation_space.nvec
action_space_size = env.action_space.n

# Define the Q-table
q_table = np.zeros((np.prod(observation_space_size), action_space_size))
# Define the learning rate, discount factor and exploration rate.
alpha = 0.1
gamma = 0.9
epsilon = 0.1

# Define the num of episodes and steps per episode
episodes = 1000
steps = 100

# Define the metric list to plot
mean_reward_per_episode = []
rewards_per_episode = []
number_of_steps_to_complete = []

for episode in range(episodes):
    # Reset the environment and get the initial state
    print("EPISODE {}".format(episode))
    state = env.reset()
    state_idx = np.ravel_multi_index(state, observation_space_size)
    
    rewards = []

    for step in range(steps):
        print("\tSTEP{}".format(step))
        # env.render()

        # Choose an action using an epsilon-greedy policy
        if random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(q_table[state_idx, :])
        
        # Take the action and get the next state, reward, and done flag
        next_state, reward, done, _ = env.step(action)
        next_state_idx = np.ravel_multi_index(next_state, observation_space_size)

        # Update the Q-table
        q_table[state_idx][action] = (1 - alpha) * q_table[state_idx][action] + alpha * (reward + gamma * np.max(q_table[next_state_idx]))
        
        # Update the state
        state = next_state

        rewards.append(reward)
        
        # Check if the episode is done
        if done:
            break
    mean_reward_per_episode.append(np.mean(rewards))
    rewards_per_episode.append(reward)
    number_of_steps_to_complete.append(step)


# Create a single figure with two subplots
fig, ax = plt.subplots(1, 2)

# Plot the data in the first subplot
ax[0].plot(mean_reward_per_episode)
ax[0].set_title("Mean reward per Episode")

# Plot the data in the second subplot
ax[1].plot(number_of_steps_to_complete)
ax[1].set_title("Steps to complete episode")

# Show the figure
plt.show()



