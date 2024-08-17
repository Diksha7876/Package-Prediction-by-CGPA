from tkinter import *
import joblib
import numpy as np

model=joblib.load("package_predictor.joblib")

def fun():
    cgpa=float(e1.get())
    arr=np.array(cgpa)
    reshaped=arr.reshape(-1,1)
    pkg=model.predict(reshaped)[0]  # we have written here [0] because it is in tuple or 2D form so we get here only first part
    lblshow.config(text=f"Your Predicted Package is : {str(pkg)[:4]} Lakhs")


a=Tk()
a.title('Package Predictor')
a.geometry('600x270')
a.config(background='lightgreen')

l1=Label(a,text='Package Predictor',font=('Robort',30,'bold'),bg='#60bd3a')
l1.pack(ipady=10,fill='x')

e1=Entry(a,font=('Robort',20))
e1.pack(pady=15)

b=Button(a,text="Predict",font=('Robort',15),bg='#164702',fg='#60bd2a',command=fun)
b.pack()

lblshow=Label(a,text="",font=('Robort',19),fg='#164702',bg='lightgreen')
lblshow.pack(pady=15)

a.mainloop()