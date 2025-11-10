# pip install hmmlearn matplotlib
import numpy as np
import matplotlib.pyplot as plt
from hmmlearn import hmm

states = ["Sunny", "Rainy"]
n_states = len(states)

observations = ["Dry", "Wet"]
n_observations = len(observations)

startprob = np.array([0.6, 0.4])
transmat = np.array([[0.7, 0.3],
                     [0.3, 0.7]])
emissionprob = np.array([[0.9, 0.1],
                         [0.2, 0.8]])

model = hmm.CategoricalHMM(n_components=n_states, random_state=42)
model.startprob_ = startprob
model.transmat_ = transmat
model.emissionprob_ = emissionprob

obs_seq = np.array([0,1,0,1,0,0]).reshape(-1,1)
hidden_states = model.predict(obs_seq)

print("Most likely hidden states (indices):", hidden_states)
logprob, path = model.decode(obs_seq, algorithm='viterbi')
print("Viterbi logprob:", logprob)
print("Viterbi path:", path)

plt.plot(path, '-o')
plt.xlabel('Time step')
plt.ylabel('Hidden state index (0=Sunny,1=Rainy)')
plt.title('Most likely hidden states over time')
plt.show()
