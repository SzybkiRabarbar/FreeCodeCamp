def arithmetic_arranger(problems:list[str], print_result:bool=False):
    if len(problems)>5:
        return "Error: Too many problems."
    lines=[[],[],[],[]]
    for operation in problems:
        operation=operation.split(" ")
        
        if operation[1]!="+" and operation[1]!="-":
            return "Error: Operator must be '+' or '-'."
        elif not operation[0].isnumeric() or not operation[2].isnumeric():
            return "Error: Numbers must only contain digits."
        
        if len(operation[0])>len(operation[2]):
            max_len=len(operation[0])
        else:
            max_len=len(operation[2])
            
        if max_len>4:
            return "Error: Numbers cannot be more than four digits."
            
        lines[0].append(f"{operation[0]:>{max_len+2}}")
        lines[1].append(f"{operation[1]}{operation[2]:>{max_len+1}}")
        lines[2].append(f"{''.join(['-' for _ in range(max_len+2)])}")
        if print_result:
            if operation[1]=="+":
                result=int(operation[0])+int(operation[2])
            else:
                result=int(operation[0])-int(operation[2])
            lines[3].append(f"{result:>{max_len+2}}")
            
    
    for id,line in enumerate(lines):
        lines[id]='    '.join(line)
    
    return '\n'.join([l for l in lines if l])
    
if __name__=="__main__":
    print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49","1 + 1"], True))