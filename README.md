# Advance-Python-World
advance python strategies you must know



1. state design pattern

let's image you have a class with multiple states , each state having it's own set of logics to 
handle the object . One method to handle this development is to code every state logics inside the
object class , but that violates the SOLID design principle pattern. 

* best approch to go is to follow state design pattern

* define each state definition into a class/dataclass 

follow the 
```
state_pattern/state_design.py
```
python file to get familiar with the implementation stratergy.


2. protocol vs abstract classes

> abstract class

* abstract classes provide coupling of the methods available for inheritance , which also provider methods for sub classes , which no need to repeat inside subclass

> protocol class

* protocol is mainly depend of structural typing. Also helps to reduce the coupling of other different classes , and abstract out the unwanted methods and attributes which we get from inheritance. We can define protocol class with only methods available for specific script. 

* also protocols helps to restrict the definition of interfaces. helps with ```interface segregation``` under SOLID design patterns. Protocols defines interfaces which other classes expect from it. reduce coupling between different modules.

* you can define same protocol inside multiple files.