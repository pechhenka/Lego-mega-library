def P(id,error):
    return error*KP[id]
def I(id,error):
    integral[id] += error
    if (abs(integral[id]) > MaxIntegraStorage):
        integral[id] = sign(integral[id])*MaxIntegraStorage
    return integral[id]*KI[id]
def D(id,error):
    temp = error-last_error[id]
    last_error[id] = error
    return temp*KD[id]
def PID(id,error):
    return P(id,error) + I(id,error) + D(id,error)