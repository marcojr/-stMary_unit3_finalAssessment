import unittest
import sys

# Garante que conseguimos importar corretamente
sys.path.insert(0, '.')

# Carrega os testes do arquivo específico
loader = unittest.TestLoader()
suite = loader.discover('tests', pattern='test_allocator.py')

# Executa com exibição de prints
runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=2)
runner.run(suite)
