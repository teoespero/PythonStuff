import tkinter
# import the objects for the GUI

############################
class MyFrame(tkinter.Frame):

    ############################
    def __init__(self, controller):

        tkinter.Frame.__init__(self)
        self.controller=controller    # saves a reference to the controller so that we can call methods
                                        # on the controller object when the user generates events
        # input area
        self.myLabel01=tkinter.Label(text='Value to Convert :')
        self.entry=tkinter.Entry()
        self.entry.insert(0, '0.00')
        self.entry['width']=25
        self.myLabel01.grid(row=1, column=0, padx=5, pady=10)
        self.entry.grid(row=1,column=1,padx=5, pady=10)

        # reset button
        self.clearBtn = tkinter.Button()
        self.clearBtn['text'] = 'Reset'
        self.clearBtn['width'] = 20
        self.clearBtn['command'] = self.controller.buttonPressedReset
        self.clearBtn.grid(row=1, column=2, padx=10, pady=10)

        # CtoF button
        self.CtoFbtn=tkinter.Button()
        self.CtoFbtn['text']='Celsius to Fahrenheit'
        self.CtoFbtn['width']=20
        self.CtoFbtn['command']=self.controller.buttonPressedCtoF
        self.CtoFbtn.grid(row=2,column=0,padx=10, pady=10)

        # FtoC button
        self.FtoCBtn=tkinter.Button()
        self.FtoCBtn['text']='Fahrenheit to Celsius'
        self.FtoCBtn['width']=20
        self.FtoCBtn['command']=self.controller.buttonPressedFtoC
        self.FtoCBtn.grid(row=2, column=1, padx=10, pady=10)

        # Quit button
        self.quitButton = tkinter.Button()
        self.quitButton['text']='Quit'
        self.quitButton['width']=20
        self.quitButton['command']=self.quit
        self.quitButton.grid(row=2, column=2, padx=10, pady=10)

        # Converted value
        self.labelForOutput=tkinter.Label()
        self.labelForOutput['text']='Converted Value: '

        self.valueForOutput=tkinter.Label()
        self.valueForOutput['anchor'] = 'w'
        self.valueForOutput['text']='0.00'
        self.valueForOutput['bg']='yellow'
        self.valueForOutput['relief']='sunken'
        self.valueForOutput['width']=20

        self.labelForOutput.grid(row=3, column=0, padx=10, pady=10)
        self.valueForOutput.grid(row=3, column=1, padx=10, pady=10)
    ############################
