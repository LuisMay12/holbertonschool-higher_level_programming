#!/usr/bin/env python3
"""
Defines an abstract class Animal and its concrete subclasses Dog and Cat.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an Animal."""

    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by subclasses."""
        pass


class Dog(Animal):
    """Concrete class Dog inheriting from Animal."""

    def sound(self):
        """Return the sound a dog makes."""
        return "Bark"


class Cat(Animal):
    """Concrete class Cat inheriting from Animal."""

    def sound(self):
        """Return the sound a cat makes."""
        return "Meow"
