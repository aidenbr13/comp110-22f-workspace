"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "7303020104"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other_point: Point) -> float:
        """Calculating the distance between two Points."""
        d: float = sqrt((self.y - other_point.y) ** 2 + (self.x - other_point.x) ** 2)
        return d


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """Updates the cell over time through one step at a time."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()
        
    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable():
            return "gray"
        elif self.is_infected():
            return "red"
        elif self.is_immune():
            return "green"

    def contract_disease(self) -> None:
        """Assigning the infected constant to the sickness attribute of the cell."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> None:
        """Assigns a cell to be TRUE if it is vulnerable."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False

    def is_infected(self) -> None:
        """Assigns a cell to be TRUE if it is infected."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False 

    def contact_with(self, other_cell: Cell):
        """Changing the state of a cell to infected when it xxxxx."""
        if self.is_infected() and other_cell.is_vulnerable():
            other_cell.contract_disease()
        elif self.is_vulnerable() and other_cell.is_infected():
            self.contract_disease()

    def immunize(self):
        """Changing the state of cell to immmune."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """Determining if the cell is immune."""
        if self.sickness == constants.IMMUNE:
            return True


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infection_start: int, immune_cells: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        count_infected: int = 0
        count_immune: int = 0
        if infection_start <= 0 or infection_start >= cells:
            raise ValueError("Incorrect number of infected cells to start.")
        if immune_cells < 0 or immune_cells >= cells:
            raise ValueError("Incorrect number of immune cells to start.")
        for i in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            if count_infected < infection_start:
                cell.contract_disease()
                count_infected += 1
            elif count_immune < immune_cells:
                cell.immunize()
                count_immune += 1
            self.population.append(cell)
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= 1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.x *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= 1.0

    def check_contacts(self) -> None:
        """Checking if cells have came into contact."""
        for y in range(len(self.population)):
            i: int = y + 1
            for x in range(i, len(self.population)):
                if self.population[y].location.distance(self.population[x].location) <= constants.CELL_RADIUS:
                    self.population[y].contact_with(self.population[x])

    def is_complete(self) -> bool:
        """Checking if the cells in population are all immune or vulnerable in order to end the simulation."""
        infected_cells: int = 0
        for cell in self.population:
            if cell.is_infected():
                infected_cells += 1
        if infected_cells >= 1:
            return False
        else:
            return True