from uiadaptationenv import UIAdaptationEnv
import numpy as np
import plotly as plt

import gym

# 1. Load Environment and Q-table structure
env = UIAdaptationEnv()
#env = gym.make('FrozenLake8x8-v1')
#Q = np.zeros([env.observation_space.n,env.action_space.n])
Q = np.zeros([env.observation_space.n,env.action_space.n])

# env.observation.n, env.action_space.n gives number of states and action in env loaded
# # 2. Parameters of Q-learning
eta = .628
gma = .9
epis = 5000
rev_list = [] # rewards per episode calculate

# 3. Q-learning Algorithm

for i in range(epis):
    # Reset environment
    s = env.reset()
    rAll = 0
    d = False
    j = 0
    #The Q-Table learning algorithm
    while j < 99:
        env.render()
        j+=1
        # Choose action from Q table
        randomNum = np.random.randn(1,env.action_space.n)
        peso = (1./(i+1))
        a = np.argmax(Q[s,:] +randomNum*peso)
        #Get new state & reward from environment
        s1,r,d,_ = env.step(a)
        #Update Q-Table with new knowledge
        print("---------------------")
        print("---------------------")
        print(s)
        print("Q[s,:]: ",Q[s,:])
        print("random: ", randomNum)
        print("peso: ", peso)
        print("mult ", randomNum*peso)
        print("Q[s,:] + mult: ",Q[s,:] + randomNum*peso)
        print("ARRAY_SHAPE", Q[s,:].shape)
        print("argmax: ",np.argmax(Q[s,:] + randomNum*peso))

        
        print(env.action_space.n)
        print("s: ", s)
        print("a: ", a)
        print(Q[s,a])
        print(i)
        print("---------------------")
        print("---------------------")

        Q[s,a] = Q[s,a] + eta*(r + gma*np.max(Q[s1,:]) - Q[s,a])
        rAll += r
        s = s1
        if d == True:
            break
    rev_list.append(rAll)
    env.render()
print("Reward Sum on all episodes " + str(sum(rev_list)/epis))
print("Final Values Q-Table")
print(Q)


'''


             
alpha = 0.7 #learning rate                 
discount_factor = 0.618               
epsilon = 1                  
max_epsilon = 1
min_epsilon = 0.01         
decay = 0.01

train_episodes = 2000    
test_episodes = 100          
max_steps = 100

#Initializing the Q-table

# Q = np.zeros((env.observation_space.n, env.action_space.n))
Q = np.zeros((len(env.observation_space.sample()), env.action_space.n))


#Creating lists to keep track of reward and epsilon values

training_rewards = []  
epsilons = []

for episode in range(train_episodes):
    #Reseting the environment each time as per requirement
    state = env.reset()    
    #Starting the tracker for the rewards
    total_training_rewards = 0


for step in range(test_episodes):
    #Choosing an action given the states based on a random number
    exp_exp_tradeoff = np.random.uniform(0, 1)
    
    ### STEP 2: SECOND option for choosing the initial action - exploit     
    #If the random number is larger than epsilon: employing exploitation 
    #and selecting best action 
    if exp_exp_tradeoff > epsilon:
        action = np.argmax(Q[state,:])
        
    ### STEP 2: FIRST option for choosing the initial action - explore       
    #Otherwise, employing exploration: choosing a random action 
    else:
        action = env.action_space.sample()
    ### STEPs 3 & 4: performing the action and getting the reward     

    #Taking the action and getting the reward and outcome state
    new_state, reward, done, info = env.step(action)
    ### STEP 5: update the Q-table

    #Updating the Q-table using the Bellman equation

    print("-----------")
    print("-----------")
    print(Q)
    print(state)
    print(action)
    print("-----------")
    print("-----------")

    Q[state, action] = Q[state, action]+alpha*(reward+discount_factor*np.max(Q[new_state,:])-Q[state, action])
    #Increasing our total reward and updating the state
    total_training_rewards += reward
    state = new_state
    
    #Ending the episode
    if done == True:
        #print ("Total reward for episode {}: {}".format(episode, 
        #total_training_rewards))
        break

    #Cutting down on exploration by reducing the epsilon 
    epsilon = min_epsilon+(max_epsilon-min_epsilon)*np.exp(-decay*episode)
    
    #Adding the total reward and reduced epsilon values
    training_rewards.append(total_training_rewards)
    epsilons.append(epsilon)
print ("Training score over time: " + str(sum(training_rewards)/train_episodes))

#Cutting down on exploration by reducing the epsilon 

epsilon = min_epsilon+(max_epsilon-min_epsilon)*np.exp(-decay*episode)

#Adding the total reward and reduced epsilon values
training_rewards.append(total_training_rewards)
epsilons.append(epsilon)
    
print ("Training score over time: " + str(sum(training_rewards)/train_episodes))

'''


#Visualizing results and total reward over all episodes
x = range(train_episodes)
plt.plot(x, training_rewards)
plt.xlabel('Episode')
plt.ylabel('Training total reward')
plt.title('Total rewards over all episodes in training') 
plt.show()

#Visualizing the epsilons over all episodes
plt.plot(epsilons)
plt.xlabel('Episode')
plt.ylabel('Epsilon')
plt.title("Epsilon for episode")
plt.show()

'''
env = UIAdaptationEnv()

steps = 0
done = False
while not done:
    # state = env.reset()
    action = env.action_space.sample()
    state, reward, done, info = env.step(action)
    steps +=1

print("TOTAL STEPS TO ADAPT: {}".format(steps))
'''
