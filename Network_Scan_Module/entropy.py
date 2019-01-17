import math
from collections import Counter

def calculate_entropy(symbol_list):
    entropy = 0
    total_symbol_count = float(len(symbol_list))
    values_symbol = Counter(symbol_list).values() # counts the elements' frequency

    for symbol_count in values_symbol:
        percentage = symbol_count/total_symbol_count
        reverse_percentage = total_symbol_count/symbol_count
        entropy += percentage * math.log(reverse_percentage,2)

    return entropy