import countdown as cd
import stopwatch as sw
import time
import Tkinter as tk
from functools import partial

        
class Cdapp(object):
    def __init__(self):
        self.mycountdown = cd.Countdown((0,0,3,0), sw.real_time)
        self.mytimer = sw.Stopwatch(sw.real_time)
        #convert countdown_time (which is in seconds) to a tuple
        self.countdown_time = self.mytimer.convert_time(self.mycountdown.countdown_time)
        self.root = tk.Tk()
        self.root.title("Countdown")
        
        self.on_state = False
        
        self.textvar = tk.StringVar()
        print self.countdown_time
        self.output = "{:02d}:{:02d}:{:02d}".format(int(self.countdown_time[0]), int(self.countdown_time[1]), int(self.countdown_time[2]))
        self.textvar.set(self.output)
        self.label = tk.Label(textvariable=self.textvar, font=("Arial",16)).grid(row=0, column=0)
        
        self.small_text = tk.StringVar()
        self.small_output = "000"
        self.small_text.set(self.small_output)
        self.small_label = tk.Label(textvariable=self.small_text, width=5, font=("Arial",8)).grid(row=0, column=0, sticky="e")
      
        self.frame = frame = tk.Frame(self.root)
        frame.grid()
        
        self.start_button = tk.Button(frame, text="START", fg="green", width=5, command=self.start).grid(row=1, column=0)
        self.stop_button = tk.Button(frame, text="STOP", fg="red", width=5, command=self.stop).grid(row=1, column=1)
        self.reset_button = tk.Button(frame, text="RESET", fg="orange", width=5, command=self.reset).grid(row=1, column=2)
        self.quit_button = tk.Button(frame, text="QUIT", width=5, command = self.root.quit).grid(row=1, column=3)
        
        self.time_left = 0
        
        #lf = tk.LabelFrame(self.root, text="Keypad", bd=3, 
        #                   relief=tk.RIDGE).grid(columnspan=3)
        self.button_list = [
        '1','2','3',
        '4','5','6',
        '7','8','9',
        '0']
        row = 4
        column = 1
        n = 0
        number_button = list(range(len(self.button_list)))
        for label in self.button_list:
            button_command = partial(self.callback, label)
            number_button[n] = tk.Button(self.frame, text=label, width=5, command=button_command)
            number_button[n].grid(row=row, column=column)
            n += 1
            column += 1
            if column > 3:
                column = 1
                row +=1
            if n == 9:
                column = 2
                
    def callback(self, label):
        print "Click {}".format(label)

    def print_elapsed(self):
        if self.on_state == True:
    
            self.time_left = self.mytimer.format_time(self.mytimer.convert_time(self.mycountdown.time_remaining()))
            self.output = self.time_left[0]
            self.small_output = self.time_left[1]
            self.textvar.set(self.output)
            self.small_text.set(self.small_output)
            
            #print "this is the time remaining {}" .format(self.mycountdown.time_remaining())
            
            if self.mycountdown.time_remaining() < 0:
                self.stop()
                
            self.root.after(50, self.print_elapsed)
            
            
        else:
            
            self.textvar.set(self.output)
            self.small_text.set(self.small_output)
        
    def start(self):
        self.mycountdown.start_countdown()
        self.on_state = True
        self.print_elapsed()
        
        
    def stop(self):
        self.mycountdown.stop_countdown()
        self.on_state = False
        self.print_elapsed()
        self.output = "00:00:00"
        self.small_output = "000"
        self.textvar.set(self.output)
        self.small_text.set(self.small_output)
        return
        
        
    def reset(self):
        self.mycountdown.reset_countdown()
        self.on_state = False
        self.output = "{:02d}:{:02d}:{:02d}".format(int(self.countdown_time[0]), int(self.countdown_time[1]), int(self.countdown_time[2]))
        self.small_output = "000"
        self.print_elapsed()
        
   
def main():
    """Run main."""
    
    a = Cdapp()
    a.root.mainloop()

    return 0

if __name__ == '__main__':
    main()
