class Strategy:
    def execute(self, data):
        pass

class ConcreteStrategyA(Strategy):
    def execute(self, data):
        print(f"Strategy A: {data}")

class ConcreteStrategyB(Strategy):
    def execute(self, data):
        print(f"Strategy B: {data}")

class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def execute_strategy(self, data):
        self._strategy.execute(data)

context = Context(ConcreteStrategyA())
context.execute_strategy("data")  # Output: Strategy A: data

context.set_strategy(ConcreteStrategyB())
context.execute_strategy("data")  # Output: Strategy B: data
