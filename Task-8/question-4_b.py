""" 4. Part - B : LED , Plasma

Inherit a TV class add additional properties like screen thickness, energy usage , Lifespan , Refresh rate ,
functionalities like viewingAngle , Backlight, DisplayDetails , which displays the detailed features of the TV
"""
class TVClass:
    def __init__(self, brand, channel , price , inches , On_OFF_status, volume):
        self.brand = brand
        self.channel = channel
        self.price = price
        self.inches = inches
        self.On_OFF_status = On_OFF_status
        self.volume = volume
class Led(TVClass):
    def __init__(self,brand, channel , price , inches , On_OFF_status, volume,
                   screen_thickness, energy_usage , Lifespan , Refresh_rate):
        # super - inherit the properties and method from parent class to child class - function under child (calling parent class) and adding one more parameter
        super().__init__(brand, channel , price , inches , On_OFF_status, volume)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.Lifespan = Lifespan
        self.Refresh_rate = Refresh_rate
class Plasma(Led):
    def __init__(self,brand, channel , price , inches , On_OFF_status, volume,
                   screen_thickness, energy_usage , Lifespan , Refresh_rate,
                      viewingAngle , Backlight, DisplayDetails):
        super().__init__(brand, channel , price , inches , On_OFF_status, volume,
                   screen_thickness, energy_usage , Lifespan , Refresh_rate,)
        self.viewingAngle = viewingAngle
        self.Backlight = Backlight
        self.DisplayDetails = DisplayDetails
    def detailed_features(self):
        print("Detailed_Features of Tv are:","Brand:",self.brand,",","Channel:",self.channel,",","Price:",self.price,",",
              "Inches:",self.inches,",","On_OFF_status:",self.On_OFF_status,",","Volume:",self.volume,",","Screen_thickness:",
              self.screen_thickness,",","Energy_usage:",self.energy_usage,",","Lifespan:",self.Lifespan,",","Refresh_rate:",
              self.Refresh_rate,",","DisplayDetails:",self.DisplayDetails,",","ViewingAngle:",self.viewingAngle,",","Backlight:",
              self.Backlight,",","DisplayDetails:",self.DisplayDetails)

obj = Plasma("Panasonic",8, 25000,32, "OFF",75,
             "6mm","50watts","11years","60Hz",
             "178 degrees","Direct LED","1920 x 1080 pixels")
obj.detailed_features()