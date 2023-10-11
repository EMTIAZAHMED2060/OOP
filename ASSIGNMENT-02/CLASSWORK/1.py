def BMI(height, weight):
    height = height/100
    BMI= round(weight/height**2,1) 
    st=''
    if BMI < 18.5:
        st+= 'Underweight'
    elif 24.9 >=BMI  >=18.5 :
        st+= 'Normal'
    elif 30 >= BMI >=25:
        st+= 'Overweight'
    else :
        st+='Obese'
    return (f"Score is {BMI}. You are {st}")
print(BMI(175,96))
    
    