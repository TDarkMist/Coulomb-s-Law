import numpy as np

k = 9 * 10**9

class PointCharge:
    def __init__(self, position, charge, velocity, mass):
        self.pos = np.array(position, dtype=float)
        self.q = charge
        self.mass = mass
        self.vel = np.array(velocity, dtype=float)

    def update_position(self, dt):
        self.pos += self.vel * dt

    def apply_force_from(self, other, dt):
        force = self.Force_from(other)
        self.vel += force / self.mass * dt

    def distance_vector(self, other):
        return self.pos - other.pos

    def Force_from(self, other):

        r_vec = self.distance_vector(other)
        r = np.linalg.norm(r_vec)

        if r == 0:
            return np.zeros(2)

        direction = r_vec / r
        magnitude = k * self.q * other.q / r**2

        return magnitude * direction


