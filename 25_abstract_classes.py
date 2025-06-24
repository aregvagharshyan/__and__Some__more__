from abc import ABC, abstractmethod
from train import TrainedModel1, TrainedModel2
from run import RunDecisionModel, RunNeuralModel

class MlModelStrategy(ABC):
    @abstractmethod
    def train(self):
        pass
    @abstractmethod
    def predict(self, inputs):
        pass
    @abstractmethod
    def evaluate(self, test_data):
        pass

class DecisionStrategy(MlModelStrategy):
    def __init__(self, data):
        if data is None:
            raise ValueError("Expected a data provider with .TrainedModel1() method")
        self.data = data
    def train(self):
        local_data = self.data.TrainedModel1()
        if local_data:
            return f'Is on!'
        return f'gone wrong!'
    def predict(self, inputs):
        local_outputs = RunDecisionModel(inputs)
        if local_outputs:
            return f'Answer: {local_outputs}'
        raise ValueError('Can\'t run the model!')
    def evaluate(self, test_data):
        return f'Some output for {test_data}.'

class NeuralNetworkStrategy(MlModelStrategy):
    def __init__(self, data):
        if data is None:
            raise ValueError("Expected a data provider with .TrainedModel1() method")
        self.data = data
    def train(self):
        local_data = self.data.TrainedModel2()
        if local_data:
            return f'Is on!'
        return f'gone wrong!'
    def predict(self, inputs):
        local_outputs = RunNeuralModel(inputs)
        if local_outputs:
            return f'Answer: {local_outputs}'
        raise ValueError('Can\'t run the model!')
    def evaluate(self, test_data):
        return f'Some output for {test_data}.'


def run(strategy, data, inputs = '', test_data = ''):
    constructed_strategy = strategy(data)
    train = constructed_strategy.train()
    predict = constructed_strategy.predict(inputs)
    evaluate = constructed_strategy.evaluate(test_data)
    return f'Predict: {predict}.\nEvaluated test - {evaluate}' if train else f'Trained successfully!'

result = run(DecisionStrategy, data = None)
print(result)

#
##
### Another One
##
#

from abc import ABC, abstractmethod

class DataPlugin(ABC):
    @abstractmethod
    def read(self):
        pass
    @abstractmethod
    def transform(self, data):
        pass
    @abstractmethod
    def write(self, data):
        pass

class CSVPlugin(DataPlugin):
    def __init__(self, data):
        self.data = data
    def read(self):
        print(self.data)
        return self.data
    def transform(self, data):
        return print(f'some logic from here! {data}')
    def write(self, data):
        return print(f'and some logic from here! {data}')

class JSONPlugin(DataPlugin):
    def __init__(self, data):
        self.data = data
    def read(self):
        print(self.data)
        return self.data
    def transform(self, data):
        return print(f'other logic from here! {data}')
    def write(self, data):
        return print(f'and some other logic from here! {data}')

data = ["name,age", "Alice,30", "Bob,25"]

def accept(plugin):
    read = plugin.read()
    transform = plugin.transform(data)
    write = plugin.write(data)
    return f'''Look at data: {read},
Transform logic: {transform}, 
Logic to write: {write}'''

csv_plugin = CSVPlugin(data)
result = accept(csv_plugin)
print(result)




