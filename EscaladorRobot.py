 #!/usr/bin/env python3
'''
    The SampleRobot class is the base of a robot application that will
    automatically call your Autonomous and OperatorControl methods at
    the right time as controlled by the switches on the driver station
    or the field controls.
    
    WARNING: While it may look like a good choice to use for your code
    if you're inexperienced, don't. Unless you know what you are doing,
    complex code will be much more difficult under this system. Use
    IterativeRobot or Command-Based instead if you're new.
'''


import wpilib
from wpilib.drive import DifferentialDrive 
controlDelDriver={“B1”:1,”B2”:2}

class MyRobot(wpilib.SampleRobot):
    '''Main robot class'''
    
    def robotInit(self):
        '''Robot-wide initialization code should go here'''
        
         self.lstick = wpilib.Joystick
        
        self.motor_D1 = wpilib.VictorSP(3)
        self.motor_I1 = wpilib.VictorSP(4)
        self.motor_externo=wpilib.VictorSP(5)
        self.G_motor=SpeedControllerGroup(self.motor_D1, self.motor_I1)
       #motor_D1 y motor_D2 son los motores de la caja de reducción 

	 
	    self.finalCarrera1=wpilib.digitalInput()
	    self.finalCarrera2=wpilib.digitalInput()

        self.robotdrive = wpilib.drive.differentialdrive(self.motor_D1, self.motor_I1)

        
    def disabled(self):
        '''Called when the robot is disabled'''
        

    def autonomous(self):
        '''Called when autonomous mode is enabled'''
        
       

    def operatorControl(self):
        '''Called when operation control mode is enabled'''


        while self.isOperatorControl() and self.isEnabled():

            # Move a motor with a Joystick
            self.motor.set(self.lstick.getY())

            while self.isOperatedControl() and self.isEnabled():
 	            if self.lstick.GetRawButton(controlDelDriver["B2"]):
                    self.motor_externo.set(1)             

            if self.lstick.GetRawButton(controlDelDriver[“B1”]):
                	self.G_motor.set(-0.7)
           	    if self.finalCarrera1.get(1)^self.finalCarrera2.get(1):
                    self.G_motor.set(-0.5)
 


if __name__ == '__main__':
    wpilib.run(MyRobot)

