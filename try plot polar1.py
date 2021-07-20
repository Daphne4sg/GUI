
    # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tkinter as tk
import tkinter.messagebox
import numpy as np
import matplotlib.pyplot as plt

class GUI:
   def __init__(self):
       self.main_window=tk.Tk()
       
       self.top_frame=tk.Frame(self.main_window)
       self.bottom_frame=tk.Frame(self.main_window)
       
       self.prompt_label1=tk.Label(self.top_frame,text='Enter the start angle theta:')
       self.n_entry1=tk.Entry(self.top_frame,width=10)
       self.prompt_label2=tk.Label(self.top_frame,text='Enter the end angle theta:')
       self.n_entry2=tk.Entry(self.top_frame,width=10)
       self.prompt_label1.pack()
       self.n_entry1.pack()
       self.prompt_label2.pack()
       
       self.n_entry2.pack()
       
       self.plot_button=tk.Button(self.bottom_frame,text='plot',command=self.plot)
       self.quit_button=tk.Button(self.bottom_frame,text='Exit',command=self.main_window.destroy)
                                                    
       self.plot_button.pack(side='left')
       self.quit_button.pack(side='left')
       
       self.top_frame.pack()
       self.bottom_frame.pack()
       
       tk.mainloop()
   def plot(self):
       st_theta=float(self.n_entry1.get())
       end_theta=float(self.n_entry2.get())
       
       theta=np.linspace(st_theta,end_theta,361)
       y=5*np.cos(theta)
       fig=plt.figure()
       plt.subplot(221,projection='polar')
       plt.plot(theta,y,lw=2)
       #plt.xlabel("X")
       #plt.ylabel("Y")
       plt.show()
3
       
       #tk.messagebox.showinfo('Results'+str(kilo)+'km is equal to'+str(miles)+'miles')
ans=GUI()
        
  
    
    
    