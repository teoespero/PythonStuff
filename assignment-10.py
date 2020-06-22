import tkinter      # the GUI objects
import windows      # the VIEW
import converter    # the MODEL

############################
class Controller:

    ############################
    def __init__(self):
        # initialize our window object

        root = tkinter.Tk()
        root.title('Temperature Converter v1.0')
        root.geometry('515x140')
        root.resizable(False, False)
        self.model = converter.Converter()
        self.view = windows.MyFrame(self)
        self.view.mainloop()
    ############################

    ############################
    def buttonPressedFtoC(self):
        # event handler when the FtoC button is pressed

        x1 = self.view.entry.get()
        self.model.FtoC(float(x1))
        self.view.valueForOutput['text'] = self.model
    ############################

    ############################
    def buttonPressedCtoF(self):
        # event handler when the CtoF button is pressed

        x1 = self.view.entry.get()
        self.model.CtoF(float(x1))
        self.view.valueForOutput['text'] = self.model
    ############################

    ############################
    def buttonPressedReset(self):
        # event handler when the reset button is pressed
        self.view.valueForOutput['text'] = '0.00'

        self.view.entry.delete(0,tkinter.END)
        self.view.entry.insert(0, '0.00')
    ############################


############################
# main file
if __name__ == '__main__':
    myController = Controller()

############################