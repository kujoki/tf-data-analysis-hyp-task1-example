import pandas as pd
import numpy as np
from scipy.stats import norm


chat_id = 670223087 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
            x_cnt: int, 
            y_success: int, 
            y_cnt: int) -> bool:
  p1 = x_success / x_cnt
  p2 = y_success / y_cnt
  p = (x_success + y_success) / (x_cnt + y_cnt)
  d = p2 - p1
  se = (p*(1-p)*(1/x_cnt + 1/y_cnt))**0.5
  z = d / se
  alpha = 0.01
  z_critical = norm.ppf(1 - alpha/2)
  if abs(z) > z_critical:
      return True # отклоняем нулевую гипотезу
  else:
      return False # не отклоняем нулевую гипотезу
