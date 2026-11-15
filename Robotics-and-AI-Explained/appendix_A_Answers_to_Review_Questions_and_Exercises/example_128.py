import statistics

def outliers(values, n_std=2.0):
    mean = statistics.mean(values)
    std = statistics.stdev(values)
    return [v for v in values
            if abs(v - mean) > n_std * std]

temps = [21.2, 21.4, 21.1, 21.3, 35.0, 21.5,
         21.2, 21.0, 21.4, 21.3]
print("outliers:", outliers(temps))
