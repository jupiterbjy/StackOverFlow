from _63758933 import module
import inspect

print(inspect.getmembers(module, inspect.isfunction))

# noinspection PyUnresolvedReferences
module.a()

module.b()


getattr(module, 'b')
