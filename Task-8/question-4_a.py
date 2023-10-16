# 4. Convert the UML diagram into a Python class and its methods.https://github.com/rvsp/typescript-oops/blob/master/Practice/TV-class.md
#Inheritance
"""TV class
TVClass - Base class
LedTV class
PlasmaTV class

Part - A

Create a TV class with properties like brand, channel , price , inches , OnOFF status and volume. Specify brand in a
constructor parameter. Channel should be 1 by default. Volume should be 50 by default.
Add methods to increase and decrease volume. Volume can't never be below 0 or above 100.
Add a method to set the channel. Let's say the TV has only 50 channels so if you try to set channel 60 the TV will
stay at the current channel.
Add a method to reset TV so it goes back to channel 1 and volume 50. (Hint: consider using it from the constructor).
It's useful to write a status that returns info about the TV status like: "Panasonic at channel 8, volume 75"."""

class TVClass:
    def __init__(self, brand, channel , price , inches , On_OFF_status, volume,reset):
        self.brand = brand
        self.channel = channel
        self.price = price
        self.inches = inches
        self.On_OFF_status = On_OFF_status
        self.volume = volume
        self.reset = reset

    def volume_status(self):
        if self.volume >=0 and self.volume <=100 and self.reset == "No":
            print("volume is: ", self.volume)
        elif self.reset == "Yes":
            print("volume is:",50)
        else:
            print("Min and max volume is 0 to 100")
    def channel_status(self,min):
        self.min = min
        if self.channel >= 1 and self.channel <= 50 and self.reset == "No":
            print("current_channel is:",self.channel)
        elif self.reset == "Yes":
            print("channel is:", self.min)
        else:
            print("Default_channel is:", self.min)

    def reset_TVstatus(self):
        if self.reset == "No":
            pass

obj = TVClass("Panasonic",8, 25000,32, "OFF",75,"No")
print(obj.brand)
obj.channel_status(1)
obj.volume_status()
obj.reset_TVstatus()