# Include your imports here, if any are used.

student_name = "Helen Rudoler"

# 1. Value Iteration
class ValueIterationAgent:
    """Implement Value Iteration Agent using Bellman Equations."""

    def __init__(self, game, discount):
        """Store game object and discount value into the agent object,
        initialize values if needed.
        """
        self.states = game.states
        self.get_actions = game.get_actions
        self.get_transitions = game.get_transitions
        self.get_reward = game.get_reward
        self.discount = discount
        # self.current_state = (0,0)
        self.values = {state:0.0 for state in self.states}

    def get_value(self, state):
        """Return value V*(s) correspond to state.
        State values should be stored directly for quick retrieval.
        """
        return self.values.get(state,0.0)

    def get_q_value(self, state, action):
        """Return Q*(s,a) correspond to state and action.
        Q-state values should be computed using Bellman equation:
        Q*(s,a) = Σ_s' T(s,a,s') [R(s,a,s') + γ V*(s')]
        """
        q_value = 0
        # print(f"transitions are: {self.get_transitions(state, action)}")
        t = self.get_transitions(state, action)
        #use t.items()
        for new_state in t:
            q_value += t[new_state] * (self.get_reward(state, action, new_state) + self.discount * self.get_value(new_state))
            # print(f"old_state: {state}, new_state: {new_state}, p: {t[new_state]}, reward: {self.get_reward(state, action, new_state)} q_value: {q_value}")
        return q_value

    def get_best_policy(self, state):
        """Return policy π*(s) correspond to state.
        Policy should be extracted from Q-state values using policy extraction:
        π*(s) = argmax_a Q*(s,a)
        """
        best_policy = None
        best_value = float('-inf')
        #game is terminal 
        for action in self.get_actions(state):     
            new_value = self.get_q_value(state, action)
            if new_value > best_value:
                best_policy = action
                best_value = new_value
        # print(f"state: {state}, best_value: {best_value}")
        return best_policy

    def iterate(self):
        """Run single value iteration using Bellman equation:
        V_{k+1}(s) = max_a Q*(s,a)
        Then update values: V*(s) = V_{k+1}(s)
        """
        #create a new empty dictionary, loop through all the states and get best policy with each state, and get q value for each
        #dict[state] = q.value
        #then reset old dictionary to new dictionary 
        best_policies = {}
        for state in self.states:
            # print(state)
            # print(self.get_best_policy(state))
            #actions may be empty
            if self.get_best_policy(state):
                best_policies[state] = self.get_q_value(state, self.get_best_policy(state))

        self.values = best_policies

#set policies to be whatever you want 
#while policies didn't change
#loop through all the states and update the best policy

# 2. Policy Iteration
class PolicyIterationAgent(ValueIterationAgent):
    """Implement Policy Iteration Agent.

    The only difference between policy iteration and value iteration is at
    their iteration method. However, if you need to implement helper function or
    override ValueIterationAgent's methods, you can add them as well.
    """

    def iterate(self):
        """Run single policy iteration.
        Fix current policy, iterate state values V(s) until |V_{k+1}(s) - V_k(s)| < ε
        """
        epsilon = 1e-6
        policy = {state:self.get_best_policy(state) for state in self.states}
        count = 100
        while True:
            count += 1
            biggest_diff = 0
            for state in self.states:

                action = policy[state]

                old_score = self.get_value(state)
                # print(action)
                # print(state)
                new_score = self.get_q_value(state, action)

                self.values[state] = new_score

                diff = abs(old_score - new_score)

                if diff > biggest_diff:
                    biggest_diff = diff

            if biggest_diff <= epsilon:
                break


# 3. Bridge Crossing Analysis
def question_3():
    discount = 0.9
    noise = 0.01
    return discount, noise

# 4. Policies
def question_4a():
    discount = 0.3
    noise = 0.0
    living_reward = 0.0
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'


def question_4b():
    discount = 0.3
    noise = 0.2
    living_reward = 0.0
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'


def question_4c():
    discount = 0.9
    noise = 0.0
    living_reward = 0.0
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'


def question_4d():
    discount = 0.9
    noise = 0.2
    living_reward = 0.0
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'


def question_4e():
    discount = 0.3
    noise = 0.0
    living_reward = 40.0
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'

# 5. Feedback
# Just an approximation is fine.
feedback_question_1 = 2.5

feedback_question_2 = """
I was confused about what policy was (a single action vs a set of actions), and also took time to understand the difference between value and q-value.
"""

feedback_question_3 = """
I definitely liked that it helped me understand MDPs, because doing this assignment made me realize that I totally did not understand it before. 
"""
