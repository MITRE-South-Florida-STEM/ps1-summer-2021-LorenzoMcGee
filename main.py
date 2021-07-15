from importlib import import_module

pss = ['ps1a', 'ps1b', 'ps1c']

for ps in pss:
  print()
  print('*'*17)
  try:
    print('running file %s' % ps)
    print('-'*17)
    globals()[ps] = import_module(ps)
  except Exception as e:
    print('\n\tError running file: %s' % ps)
    print('\tError:', e)
