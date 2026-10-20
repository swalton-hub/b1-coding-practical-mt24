def controlller(y, r, y_prev, r_prev):
    Kp = 0.15
    Kd = 0.6
    e = r - y
    e_prev = r_prev - y_prev
    u = Kp * e + Kd * (e - e_prev)
    return u