import random

student_name = "Helen Rudoler."

# 1. Q-Learning
class QLearningAgent:
    """Implement Q Reinforcement Learning Agent using Q-table."""

    def __init__(self, game, discount, learning_rate, explore_prob):
        """Store any needed parameters into the agent object.
        Initialize Q-table.
        """
        self.get_actions = game.get_actions
        self.discount = discount
        self.learning_rate = learning_rate
        self.explore_prob = explore_prob
        self.q_table = {}

    def get_q_value(self, state, action):
        """Retrieve Q-value from Q-table.
        For an never seen (s,a) pair, the Q-value is by default 0.
        """
        if (state, action) in self.q_table:
            return self.q_table[(state, action)]
        else: return 0

    def get_value(self, state):
        """Compute state value from Q-values using Bellman Equation.
        V(s) = max_a Q(s,a)
        """
        max_q_val = float('-inf')
        if not self.get_actions(state):
            return 0
        for action in self.get_actions(state):
            q_value = self.get_q_value(state, action)
            if q_value > max_q_val:
                max_q_val = q_value
        return max_q_val

    def get_best_policy(self, state):
        """Compute the best action to take in the state using Policy Extraction.
        π(s) = argmax_a Q(s,a)

        If there are ties, return a random one for better performance.
        Hint: use random.choice().
        """
        arg_max = None
        max_q_val = float('-inf')
        for action in self.get_actions(state):
            q_value = self.get_q_value(state, action)
            if q_value > max_q_val:
                arg_max = action
                max_q_val = q_value
            if q_value == max_q_val:
                arg_max = random.choice([action, arg_max])
                max_q_val = self.get_q_value(state, arg_max)
        return arg_max

    def update(self, state, action, next_state, reward):
        """Update Q-values using running average.
        Q(s,a) = (1 - α) Q(s,a) + α (R + γ V(s'))
        Where α is the learning rate, and γ is the discount.

        Note: You should not call this function in your code.
        """
        
        sample = reward + self.discount * self.get_value(next_state)
        new_q_value = (1 - self.learning_rate) * self.get_q_value(state, action) + self.learning_rate * sample
        self.q_table[(state, action)] = new_q_value
        return new_q_value

    # 2. Epsilon Greedy
    def get_action(self, state):
        """Compute the action to take for the agent, incorporating exploration.
        That is, with probability ε, act randomly.
        Otherwise, act according to the best policy.

        Hint: use random.random() < ε to check if exploration is needed.
        """
        if not self.get_actions(state):
            return None
        if random.random() < self.explore_prob:
            return random.choice(list(self.get_actions(state)))
        else: 
            return self.get_best_policy(state)


# 3. Bridge Crossing Revisited
def question3():
    # epsilon = ...
    # learning_rate = ...
    # return epsilon, learning_rate
    return 'NOT POSSIBLE'
    # If not possible, return 'NOT POSSIBLE'


# 5. Approximate Q-Learning
class ApproximateQAgent(QLearningAgent):
    """Implement Approximate Q Learning Agent using weights."""

    def __init__(self, *args, extractor):
        """Initialize parameters and store the feature extractor.
        Initialize weights table."""

        super().__init__(*args)
        self.extractor = extractor
        self.weights = {}

    def get_weight(self, feature):
        """Get weight of a feature.
        Never seen feature should have a weight of 0.
        """
        if feature in self.weights:
            return self.weights[feature]
        else: return 0

    def get_q_value(self, state, action):
        """Compute Q value based on the dot product of feature components and weights.
        Q(s,a) = w_1 * f_1(s,a) + w_2 * f_2(s,a) + ... + w_n * f_n(s,a)
        """
        feature_vector = self.extractor(state, action)
        q_value = 0
        for feature in feature_vector:
            feature_value = feature_vector[feature]
            weight = self.get_weight(feature)
            q_value += feature_value * weight
        return q_value

    def update(self, state, action, next_state, reward):
        """Update weights using least-squares approximation.
        Δ = R + γ V(s') - Q(s,a)
        Then update weights: w_i = w_i + α * Δ * f_i(s, a)
        """
        sample = reward + self.discount * self.get_value(next_state) - self.get_q_value(state, action)
        feature_vector = self.extractor(state, action)
        # weights_copy = self.weights.copy()
        for feature in feature_vector:
            feature_value = feature_vector[feature]
            updated_weight = self.get_weight(feature) + self.learning_rate * sample * feature_value
            # weights_copy[feature] = updated_weight
            self.weights[feature] = updated_weight
        # self.weights = weights_copy




# 6. Feedback
# Just an approximation is fine.
feedback_question_1 = 3

feedback_question_2 = """
Understanding the extractor was the most conceptually difficult part. 
"""

feedback_question_3 = """
I really liked the pacman gui. I also like how our agent got progressively 
smarter as we implemented more things, was cool to see the progression of the reinforecement 
algorithms. 
"""
