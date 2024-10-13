from polymorphism_demo import Shape, Rectangle, Circle


def main():
    # Create a list of different shapes
    shapes = [
        Rectangle(10, 5),  # Rectangle with length 10 and width 5
        Circle(7)          # Circle with radius 7
    ]

    # Demonstrate polymorphism by calling the area() method
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")


if __name__ == "__main__":
    main()