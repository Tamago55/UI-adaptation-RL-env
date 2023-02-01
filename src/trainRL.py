from uiadaptationenv import UIAdaptationEnv



env = UIAdaptationEnv()


steps = 0
done = False
while not done:
    # state = env.reset()
    action = env.action_space.sample()
    state, reward, done, info = env.step(action)
    steps +=1

print("TOTAL STEPS TO ADAPT: {}".format(steps))