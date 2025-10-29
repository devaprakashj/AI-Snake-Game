import matplotlib.pyplot as plt
from IPython import display

plt.ion()

def plot(scores, mean_score):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Training Progress')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores)
    plt.plot([mean_score]*len(scores))
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(scores)-1, mean_score, f'{mean_score:.2f}')
    plt.show(block=False)
    plt.pause(.1)
