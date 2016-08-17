
 
 # importeer de GPIO bibliotheek. 
 import   RPi . GPIO  as   GPIO 
 # Importeer de time biblotheek voor tijdfuncties. 
 from   time   import   sleep 
 
 # Zet de pinmode op Broadcom SOC. 
 GPIO . setmode ( GPIO . BCM ) 
 # Zet waarschuwingen uit. 
 GPIO . setwarnings ( False ) 
 print   "Druk op de knop..." 
 
 # Deze functie wordt uitgevoerd als er op de knop gedrukt is. 
 def   gedrukt ( pin ) : 
   print   "Er is gedrukt!, interrupt op pin:" ,   pin 
 
 # Deze functie is een oneindige loop en houd het script draaiend. 
 def   loop ( ) : 
   try : 
     raw_input ( ) 
   # Wanneer er op CTRL+C gedrukt wordt. 
   except   KeyboardInterrupt :   
     # GPIO netjes afsluiten 
     GPIO . cleanup ( )  
 
 # Zet de GPIO pin als ingang. 
 GPIO . setup ( 22 ,   GPIO . IN ) 
 # Gebruik een interrupt, wanneer actief run subroutinne 'gedrukt' 
 GPIO . add_event_detect ( 22 ,   GPIO . RISING ,   callback = gedrukt ,   bouncetime = 200 ) 
 
 loop ( ) 