class PheromoneTable:
    def __init__(self):
        self.table = {}

    def reinforce(self, peer, value):
        self.table[peer] = self.table.get(peer, 0) + value

    def decay(self):
        for peer in self.table:
            self.table[peer] *= 0.9

    def get_best_candidates(self, threshold):
        return [peer for peer, val in self.table.items() if val >= threshold]