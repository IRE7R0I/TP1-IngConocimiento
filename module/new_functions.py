def is_empty(value):
    if isinstance(value, (list, tuple, dict)):
         if not value:
              return True
         else:
              return False
         
         
def avg(value, count = 2):
    if isinstance(value, (list, tuple, dict)) or hasattr(value, '__iter__'):
        value = list(value)  # convierte dict_values en lista
        return sum(value) / len(value)
    elif isinstance(value, (int, float)):
         return value / count
    else:
         return None