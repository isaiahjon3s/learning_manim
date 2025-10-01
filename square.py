from manim import *

class SquareAnimation(Scene):
    def construct(self):
        square = Square(color=RED)
        self.play(Create(square))
        self.wait()
        circle = Circle(color=BLUE)
        self.play(Create(circle))
        self.wait()
        triangle = Triangle(color=GREEN)
        self.play(Create(triangle))
        self.wait()
        # FIX
        # Calculate the inscribed square size for the triangle
        # For an equilateral triangle, the inscribed square side length is:
        # side_length = triangle_height * 2 / (2 + sqrt(3))
        triangle_height = triangle.height
        inscribed_square_size = triangle_height * 2 / (2 + np.sqrt(3))
        
        square = Square(color=YELLOW, side_length=inscribed_square_size)
        # Position the square lower to fit perfectly inside the triangle
        square.move_to(triangle.get_center() + DOWN * triangle_height/3)
        
        self.play(Create(square))
        self.wait()


