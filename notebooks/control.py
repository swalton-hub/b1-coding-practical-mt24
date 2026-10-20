def controller(y, r, y_prev, r_prev):
   
    # Outputs the action of a PD controller using inputs: y as current state, r as reference, y_prev as previous state, and r_prev as previous reference.

    Kp = 0.15
    Kd = 0.6
    e = r - y
    e_prev = r_prev - y_prev
    u = Kp * e + Kd * (e - e_prev)
    return u