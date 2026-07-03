from functools import wraps

def log_activity(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    print(f"Executing {func.__name__} with arguments: {args} and keyword arguments: {kwargs}")
    result = func(*args, **kwargs)
    print(f"{func.__name__} returned: {result}")
    print(f"Finished executing {func.__name__}")
    return result
  return wrapper
  


def log_authentication(func):
  @wraps(func)
  def wrapper(user_roles):
    if user_roles != 'admin':
      print("User authenticated but does not have admin privileges.")
    else:
      return func(user_roles)
  return wrapper
  
# @log_activity
# def brew_coffee(coffee_type):
#   return f"Brewing a cup of {coffee_type}"

# brew_coffee("Espresso")

@log_authentication
def access_sensitive_data(user_roles):
  print("Accessing sensitive data...")


# access_sensitive_data("guest")
# access_sensitive_data("admin")
log_activity(access_sensitive_data)("employee")
