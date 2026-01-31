#   Abstract

This project presents the design and implementation of a Python library for solving fundamental laws of electromagnetism, including Coulomb’s law, Gauss’s law, Biot–Savart
law, and Maxwell’s equations in one, two, and three dimensions. The library is modular,
easy to use, and implemented using Python and NumPy. The correctness of the library
is verified using test scripts.


-----
##  Introduction

Electromagnetism is a fundamental branch of physics that deals with electric and magnetic phenomena. It explains interactions between electrically charged particles and the electric and magnetic fields they produce.

------
###  Fundamental Laws Of Electromagnetism
Coulomb's Law
Gauss's Law
Biot-Savart Law
Ampere's Circuital Law
Faraday's Law of electromagnetic induction

These laws were unified by James Clerk Maxwell in Maxwell's equtions.
   

------
###  Applications Of Electromagnetism

Electric power generation and transmission
Motors and Generators
Communication systems
Medical imaging
Electronics


## Objectives

To design a modular python library
To implement major electromagnetic laws
To support 1D, 2D and 3d calculations
To verify numerical corrections


## Theory

### (1) Coulomb's Law

The electrostatic force between two point charges is directly proportional to the product
of their charges and inversely proportional to the square of the distance between them.
The force acts along the line joining the two charges.

F = (1 / 4πϵ₀) × (q₁ q₂ / r²)
---


### (2) Gauss’s Law 

The total electric flux through any closed surface is equal to ε1
0
times the total electric
charge enclosed by that surface.

∮ E · dA = Q / ϵ₀

---


### (3️) Biot–Savart Law

The magnetic field at a point due to a small current element is directly proportional to
the current and the length of the element, inversely proportional to the square of the
distance from the element, and depends on the sine of the angle between the current
element and the line joining the element to the point.

dB = (μ0 / 4π) * (I * (dl × r̂)) / r²


---

### (4) Maxwell’s Equations

Maxwell’s Equations are four fundamental equations that describe how electric and magnetic fields are generated and how they interact with charges and currents.

∇ · E = ρ / ϵ₀        (Gauss’s Law – Electric) 
∇ · B = 0            (Gauss’s Law – Magnetism) 
∇ × E = −∂B/∂t       (Faraday’s Law) 
∇ × B = μ₀J + μ₀ϵ₀∂E/∂t (Ampère–Maxwell Law)

---



##  Software Design
```bash
emlib
     __init__.py
     constants.py
     coulomb.py
     gauss.py
     biot_savart.py
     maxwell.py
     
test_emlib
          test_coulomb.py
          test_gauss.py
          test_biot_savart.py
          test_maxwell.py

          



---


##  Module Description

Each module implements a specific electromagnetic law using a modular design.

---

##  Implementation 

The library is implemented using Python and NumPy. Each law is implemented as a
separate function supporting 1D, 2D, and 3D computations.

##  Results and Verification


All modules were tested using a demonstration script and produced correct numerical
results.

##  Conclusion 
A modular Python library for electromagnetic laws was successfully developed and verified. The project is suitable for educational and computational use.
