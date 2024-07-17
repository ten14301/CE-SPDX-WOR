import re

def is_valid_date(date_str):
  """
  Checks if a string is a valid date in YYYY-MM-DD format without using regular expressions.

  Args:
    date_str (str): The date string to validate.

  Returns:
    bool: True if the date is valid, False otherwise.
  """

  if not date_str or len(date_str) != 10:
    return False

  try:
    # Split the date string into year, month, and day
    year, month, day = map(int, date_str.split("-"))

    # Check for valid year range (e.g., 1000-9999)
    if year < 1000 or year > 9999:
      return False

    # Check for valid month (1-12)
    if month < 1 or month > 12:
      return False

    # Check for valid day based on month (considering leap year)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2:  # Check for leap year
      if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_in_month[1] = 29
      else:
        days_in_month[1] = 28
    if day < 1 or day > days_in_month[month - 1]:
      return False

  except ValueError:  # ValueError occurs if conversion to int fails
    return False

  return True



def is_valid_username(username, minlen):
  # Checks if the received username matches the required conditions.
  if type(username) != str:
    raise TypeError("username must be a string")
      
  if minlen < 1:
    raise ValueError("minlen must be at least 1")
   
  # Usernames can't be shorter than minlen
  if len(username) < minlen:
    return False
  
  # Usernames can only use letters, numbers, dots and underscores
  if not re.match('^[a-z0-9._]*$', username):
    return False
  
  # Usernames can't begin with a number
  if username[0].isnumeric():
    return False
  
  return True