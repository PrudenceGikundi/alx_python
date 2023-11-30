def is_prime(num):
  if num%num==0 and num%1==0:
    return True
  elif num%num>=0 and num%1<=0:
    return False
  else:
    return num