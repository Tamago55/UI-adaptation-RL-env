## Reinforcement Learning - based User Interface Adaptation

This repository will be used to show the implementation of a training environment for RL agents for the UI adaptation problem.

#### Dependencies
* Numpy `pip install numpy`
* Openai Gym `pip install gym`
* Matplotlib `pip install matplotlib`
* Keras `pip install keras`
* Tensorflow `pip install tensorflow` (see tensorflow webpage for detailed information)
* Keras-RL2 `pip install keras-rl2`

#### Run an example:
1. Go to `src` path: `cd src`
2. Test with algorithms:
  2.1 `python QLearning.py` - This will stop automatically
  2.2 `python KerasRL_DQN.py` - This will stop when you hit "Ctrl+C"

#### How to user other algorithms:

You can install libraries such as Keras-RL2, stable-baselines, RL-coach, etc. Then, create your own python program that uses an algorithm from one of these libraries and import the UIAdaptation env:

`from uiadaptationenv import UIAdaptationEnv`

and use it

`env = UIAdaptationEnv()`


#### Modify the environment and play arround:

1. You can use a `verbose` mode. When calling the `step` function, you can use the `verbose=True` to see what's happening in real time.
2. Use more/less information for the state representation:
  2.1 Change the `platform_.py`, `user.py`, `environment.py` and `uidesign.py` files in order to add/remove information for each element.
  2.2 Change the `utils.get_random_*()` functions to add/remove the informaiton added/removed in step 2.1.
  2.3 Change the `observation_space`

#### TODO

There are still some work in progress. This is a prototype.

The reward function now only works with preferences + emotions. Needs to be done: Get the usability from UI Design. Get Emotions from other sources, such as facial expressions. Etc.

The representation of the UI is now model based. There is no UI visible. We are developing an adaptable interface which will be connected to this models. This way the agents will know how to adapt the real UI.