import numpy as np

def calculate(numbers: list) -> dict[str:list]:
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")
    calculation = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum
    }
    table = np.array(numbers)
    table = table.reshape(3,3)
    for key, value in calculation.items():
        calculation[key] = apply_method(table, value)
    return calculation

def apply_method(table: np.ndarray, method: callable) -> list[list,list,float]:
    result = [[method(table[:,0]), method(table[:,1]), method(table[:,2])]]
    result.append([method(table[0]), method(table[1]), method(table[2])])
    result.append(method(table))
    return result

if __name__=="__main__":
    data = calculate([0,1,2,3,4,5,6,7,8])
    for k, v in data.items():
        print(f"{k}: {v}")