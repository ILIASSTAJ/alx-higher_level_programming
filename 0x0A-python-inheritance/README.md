Python Inheritance Basics
This directory provides an introduction to Python inheritance and covers various concepts related to superclass, subclass, attributes, methods, and built-in functions.

Superclass, Baseclass, or Parentclass
A superclass, baseclass, or parent class is a class that is being inherited from. It serves as the foundation or blueprint for creating new classes, known as subclasses. The superclass provides attributes and methods that can be inherited and reused by its subclasses.

Subclass
A subclass is a class that is derived from a superclass or baseclass. It inherits all the attributes and methods from its superclass and can also add its own attributes and methods or override the ones inherited.

Listing Attributes and Methods
To list all attributes and methods of a class or instance in Python, you can use the built-in functions dir() or vars(). The dir() function returns a list of all the valid attributes and methods of an object, while vars() returns a dictionary of the object's attributes and their values.

Adding New Attributes
An instance in Python can have new attributes at any time. You can simply assign a value to a new attribute directly to the instance.

Inheriting a Class
To inherit a class from another, you can define a new class and put the name of the superclass in parentheses after the class name.

Multiple Base Classes
You can define a class with multiple base classes using multiple inheritance. In the class definition, you list the base classes in parentheses, separated by commas.

Default Class Inheritance
The default class that every class in Python inherits from is the built-in class called object. It is the ultimate base class in Python's class hierarchy.

Method and Attribute Overriding
To override a method or attribute inherited from the base class, you define a method or attribute with the same name in the subclass.

Inherited Attributes and Methods
Subclasses inherit all the attributes and methods from their superclass(es). They can access and use these inherited attributes and methods as if they were their own. However, if a subclass defines an attribute or method with the same name as the one inherited from the superclass, it will override the inherited one.

Purpose of Inheritance
The purpose of inheritance is to promote code reuse and create a hierarchical structure among classes. It allows subclasses to inherit and extend the functionality of their superclass(es), reducing code duplication and providing a way to organize and specialize classes based on their relationships.

Built-in Functions
The following built-in functions are commonly used with inheritance in Python:

isinstance(object, class)
issubclass(class, classinfo)
type(object)
super()
Please refer to the Python documentation or the code examples in this repository for detailed usage instructions for these functions.

Feel free to explore the code examples and further expand your understanding of Python inheritance.
