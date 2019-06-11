This project aims to continuously measure the density of homebrew beer as
it ferments using an ultrasonic sensor on or in the fermentation vessel.

The current standard way of measuring density is to float a hygrometer in 
a sample of the beer. This wastes beer and draws air into the fermenter
as beer is drained into the measuring flask from the tap. Air contains
oxygen, and oxygen oxidises beer, so it is to be avoided if possible.
Additionally, it is tricky to get accurate, repeatable results using
a float hygrometer, due to bubbles forming on them during measurement.

The speed of sound is dependant on the density of the medium through which
the sound is travelling. If we measure the time of flight of an ultrasonic
ping through a fixed distance we can determine the density of the medium,
beer in this case.

Using a 160MHz clock in an ESP8266 and pin interrupts we can get a temporaral
resolution of 6.25ns, which should give us some useful data over the typical
beer fermentation density range of 1.005 to 1.050 according to rough napkin
calculations.

We aren't too concerned with absolute accuracy of the density measurement,
since we're primarily interested in the density delta. Once the density stops
changing, the fermentation is complete and the beer can be bottled.

This code is written to run on an ESP8266 and publish results to a local
MQTT broker.
