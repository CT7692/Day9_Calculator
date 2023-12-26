def yes_no_validator(option_a, option_b, prompt):
  user_input = input(prompt).lower()
  correct = True
  if user_input != option_a and user_input != option_b:
    correct = False
    while not correct:
      print("Please choose a valid option.")
      user_input = input(prompt).lower()
      if user_input == option_a or user_input == option_b:
        correct = True
  return user_input

def num_validator(prompt):
  str_num = input(prompt)
  correct = True
  if not str_num.isnumeric():
    correct = False
    while not correct:
      print("Please enter a number.")
      str_num = input(prompt)
      if str_num.isnumeric():
        correct = True
  num = float(str_num)
  return num

def operation_validator(prompt):
  math_operation = input(prompt)
  correct = True
  if (math_operation != "+") and (math_operation != "-") and (math_operation != "*") and (math_operation != "/"):
    correct = False
    while not correct:
      print("Please choose a valid operation to perform the calculation.")
      math_operation = input(prompt)
      if (math_operation == "+") or (math_operation == "-") or (math_operation == "*") or (math_operation == "/"):
        correct = True
  return math_operation

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

def div_check(operator, divisor):
  clear = True
  if operator == "/" and divisor == 0:
    clear = False
    print("Can't divide by 0.")
    
  return clear
  
def initial_operation(operation_dictionary, prompt, new_prompt):
  n1_prompt = "First Number: "
  n1 = num_validator(n1_prompt)
  print("\n")
  for i in operation_dictionary:
    print(i)
  print("\n")
  operation = operation_validator(prompt)
  n2 = num_validator(new_prompt)
  answer = 0
  if clear := div_check(operation, n2):
    calculate = operation_dictionary[operation]
    answer = calculate(n1, n2)
    print(f"{n1} {operation} {n2} = {answer}")
  else:
    answer = n1
  return answer

def continuous(val, dictionary, op_prompt, next_prompt):
  new_operation = operation_validator(op_prompt)
  new_num = num_validator(next_prompt)
  answer = 0
  if clear := div_check(new_operation, new_num):
    calculate = dictionary[new_operation]
    answer = calculate(val, new_num)
    print(f"{val} {new_operation} {new_num} = {answer}")
  else:
    answer = val
  return answer

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

y = "yes"
n = "no"
op_prompt = "Pick a mathematical operation: "
next_prompt = "Next Number: "
value = initial_operation(operations, op_prompt, next_prompt)
yes_no_prompt = f"Keep calculating with {value}? {y} or {n}: "

if (keep_going := yes_no_validator(y, n, yes_no_prompt)) == y:
  still_working = True
  while still_working:
    value = continuous(value, operations, op_prompt, next_prompt)
    yes_no_prompt = f"Keep calculating with {value}? {y} or {n}: "
    if (keep_going := yes_no_validator(y, n, yes_no_prompt)) == n:
      still_working = False
      print("See ya!")
