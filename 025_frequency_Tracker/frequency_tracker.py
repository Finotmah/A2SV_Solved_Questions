from collections import defaultdict

class FrequencyTracker:

    def __init__(self):
        self.num_freq = defaultdict(int)
        self.freq_count = defaultdict(int)

    def add(self, number: int):
        old = self.num_freq[number]

        if old:
            self.freq_count[old] -= 1
            if self.freq_count[old] == 0:
                del self.freq_count[old]

        self.num_freq[number] += 1
        new = self.num_freq[number]
        self.freq_count[new] += 1


    def deleteOne(self, number: int):
        old = self.num_freq[number]

        if not old:
            return

        self.freq_count[old] -= 1
        if self.freq_count[old] == 0:
            del self.freq_count[old]

        self.num_freq[number] -= 1
        new = self.num_freq[number]

        if new:
            self.freq_count[new] += 1


    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freq_count
