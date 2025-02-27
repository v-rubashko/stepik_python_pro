from collections import defaultdict

def best_sender(messages, senders):
    res = defaultdict(int)
    l = len(messages)
    for i in range(l):
        res[senders[i]] += len(messages[i].split(" "))
    res_max = max(sorted(res, reverse=True), key = lambda k: res[k])
    return res_max


messages = ['Hi, Linda', 'Hi, Sam', 'How are you doing?']
senders = ['Sam Fisher', 'Linda', 'Sam Fisher']

print(best_sender(messages, senders))