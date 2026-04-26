from utils import get_reward_by_profit

class Seller:
    def __init__(self, id, name, profits ):
        self.id = id
        self.name = name
        self.profits = profits

    # def __init__(self, id: None, name:None, profits:None, reward: None ):
    #     self.id = id
    #     self.name = name
    #     self.profits = profits
    #     self.reward = reward

    def add_profit(self, quarter, profit):
        """Adds a profit for a specific quarter."""
        if quarter not in self.profits:
            self.profits[quarter] = []
        self.profits[quarter].append(profit)

    def calculate_and_set_reward(self):
        """Calculates the overall GPA using the calculate_average function."""
        total_profit = sum([profit for profit in self.profits.values()])
        self.total_profit = total_profit
        self.reward = get_reward_by_profit(total_profit)

    def display_info(self):
        print(f"Seller Name: {self.name}")
        print(f"Reward: {self.reward}")
        print("----------------------------")

