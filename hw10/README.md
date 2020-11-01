## hw10 Funtionalities

### Problem I: Complex Class
#### Purpose: a class that models a complex number in the form of x+yi.

#### Functions:

##### __init__(self, real, imag):
**Purpose**: Instantiates a real number object.   
**Input Parameters**: 
self
other
real -  the real number component.
image - the imaginary number coefficient.
**Return Value**: None.

##### __str__(self):
**Purpose**: Returns a Complex object represented as a String.  
**Input Parameters**: self

##### get_real(self):
**Purpose**: Returns the real component of a given Complex object.  
**Input Parameters**: self

##### get_imag(self):
**Purpose**: Returns the imaginary component of a given Complex object.  
**Input Parameters**: self

##### set_real(self, new_real):
**Purpose**: Sets the real component of a given Complex object.  
**Input Parameters**: 
self
new_real - a new real number component to replace the current one

##### set_imag(self, new_imag):
**Purpose**: Sets the imaginary component of a given Complex object.  
**Input Parameters**: 
self
new_imag - a new imaginary number component to replace the current one

##### __add__(self, other):
**Purpose**: Adds two Complex objects  
**Input Parameters**:
self
other - another complex object
**Return Value**: the sum of the two parameters

##### __mul__(self, other):
**Purpose**: Multiplies two Complex objects  
**Input Parameters**:
self
other - another complex object
**Return Value**: the product of the two parameters

##### __eq__(self, other):
**Purpose**: Evaluates whether two Complex objects are equal 
**Input Parameters**:
self 
other - another complex object
**Return Value**:
True if the two objects are equal
False if the two objects are not equal
