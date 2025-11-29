#!/usr/bin/env python3
"""
Proyecto: Toggle LED desde ROS hacia Arduino Uno
Autor: Jesús López
Fecha: 25/11/2025
Descripción:
Este script en Python actúa como publisher en ROS. Envía mensajes
std_msgs/Bool al tópico /toggle_led, que son recibidos por el Arduino Uno
a través de rosserial. El LED conectado al pin 13 se enciende o apaga
según la tecla presionada.
Controles:
    ENTER: Encender LED
    ESPACIO: Apagar LED
Ejemplo de ejecución:
    chmod +x scripts/remote_led.py
    rosrun turtle_robot remote_led.py
"""
import rospy
from std_msgs.msg import Bool

def remote_led():
    rospy.init_node('remote_led_publisher', anonymous=True)
    pub = rospy.Publisher('/toggle_led', Bool, queue_size=10)
    
    rospy.loginfo("Presiona ENTER para encender, ESPACIO para apagar")
    
    while not rospy.is_shutdown():
        tecla = input()
        
        msg = Bool()
        
        if tecla == "":  # ENTER
            msg.data = True
            rospy.loginfo("LED ENCENDIDO")
        else:  # ESPACIO u otra tecla
            msg.data = False
            rospy.loginfo("LED APAGADO")
        
        pub.publish(msg)

if __name__ == '__main__':
    try:
        remote_led()
    except rospy.ROSInterruptException:
        pass
