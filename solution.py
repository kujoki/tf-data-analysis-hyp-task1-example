import pandas as pd
import numpy as np
from scipy.stats import norm

chat_id = 670223087 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, x_cnt: int, y_success: int, y_cnt: int) -> bool:
    p_control = x_success / x_cnt
    p_test = y_success / y_cnt
    
    se_pooled = ((p_control * (1 - p_control) / x_cnt) + (p_test * (1 - p_test) / y_cnt)) ** 0.5
    
    z_score = (p_test - p_control) / se_pooled
    
    z_critical = norm.ppf(0.01)
    
    if z_score <= z_critical:
        return True 
    else:
        return False
