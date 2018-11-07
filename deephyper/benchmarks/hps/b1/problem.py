
from deephyper.benchmarks import HpProblem

Problem = HpProblem()
Problem.add_dim('epochs', (5, 500), 5)
#bechmark specific parameters
Problem.add_dim('rnn_type', ['LSTM', 'GRU', 'SimpleRNN'], 'LSTM')
Problem.add_dim('nhidden', (1, 100), 1)
Problem.add_dim('nlayers', (1, 30), 1)
#network parameters
Problem.add_dim('activation', ['relu', 'elu', 'selu', 'tanh'], 'relu')
Problem.add_dim('batch_size', (8, 1024), 8)
Problem.add_dim('dropout', (0.0, 1.0), 0.0)
Problem.add_dim('optimizer', ['sgd', 'rmsprop', 'adagrad', 'adadelta', 'adam', 'adamax', 'nadam'], 'sgd')
#space['init'] = ['Zeros', 'Ones', 'Constant', 'RandomNormal', 'RandomUniform', 'TruncatedNormal', 'VarianceScaling', 'Orthogonal', 'Identity', 'lecun_uniform', 'glorot_normal', 'glorot_uniform', 'he_normal', 'lecun_normal', 'he_uniform']
# common optimizer parameters
#space['clipnorm'] = (1e-04, 1e01)
#space['clipvalue'] = (1e-04, 1e01)
# optimizer parameters
Problem.add_dim('learning_rate', (1e-04, 1e01), 1e-04)
#space['patience'] = (5, 100)
#space['delta'] = (0, 1e-02)
#space['momentum'] =  (0, 1e01)
#space['decay'] =  (0, 1e01)
#space['nesterov'] = [False, True]
#space['rho'] = (1e-04, 1e01)
#space['epsilon'] = (1e-08, 1e01)
#space['beta1'] = (1e-04, 1e01)
#space['beta2'] = (1e-04, 1e01)

if __name__ == '__main__':
    print(Problem)
