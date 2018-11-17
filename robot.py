
import wpilib

class MyRobot(wpilib.IterativeRobot):
    '''Main robot class'''
    
    def robotInit(self):
        '''Robot-wide initialization code should go here'''
        
        self.lstick = wpilib.xboxcontroller(0)

        self.motor_D1 = wpilib.Victorsp(1)
        self.motor_I1 = wpilib.Victorsp(2)
        self.G_motor=SpeedControllerGroup(self.motor_D1, self.motor_I1)
       
        self.robotdrive = wpilib.drive.differentialdrive(self.motor_D1, self.motor_I1)
        self.ultrasound1 = wpilib.ultrasonic(1,2 units=1)
        self.ultrasound1.SetAutomaticMode(True)

        self.ultrasound2 = wpilib.ultrasonic(3,4 units=1)
        self.ultrasound2.SetAutomaticMode(True)

        self.infrarojo = wpilib.infrared()
        #Unsure if "infrared" is a wpilib function, check 


#motor_d1 son los motores de la caja de reducción
#ultrasound1 frontal es el sensor us que se usa para detectar la barra pegada a pared mientras ultrasound2 es el que se usa para saber que tan arriba esta el robot mientras escala.

    def autonomousInit(self):
        '''Called only at the beginning of autonomous mode'''
        pass

    def autonomousPeriodic(self):
        '''Called every 20ms in autonomous mode'''
        pass

            while self.isauto
                #Elevador se mantiene at rest due to the importance of other topics

    def disabledInit(self):
        '''Called only at the beginning of disabled mode'''
        pass
    
    def disabledPeriodic(self):
        '''Called every 20ms in disabled mode'''
        pass

    def teleopInit(self):
        '''Called only at the beginning of teleoperated mode'''
        pass

    def teleopPeriodic(self):
        '''Called every 20ms in teleoperated mode'''
        
        # Move a motor with a Joystick

        if.lstick.getAbutton
        #Prob will use PS4, XBOX or Joystic

        while self.isOperatedControl() and self.isEnabled():
            If self.lstick.GetButton(Joystick["R2"])
                self.MotorGroup.set (2)
            
            If self.lstick.Get("boton")Button(("Controller") ["Boton 2"])
                #Luego definimos que boton se va a usar para el ultrasonido
                print(self.ultrasound1.getRangeMM())
                     if self.ultrasound1.getRangeMM(50)
                
self.drive.arcadeDrive(self. getY(self))self.
              ·#Check this with Pino and José bc im super confused and sleepy 
                    
        self.(self.lstick.getY())
        self.motorc.set(1)0
        
if __name__ == '__main__':
    wpilib.run(MyRobot)

