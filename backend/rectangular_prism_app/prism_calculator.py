class PrismCalculator:
    @staticmethod
    def calculate_surface_area(length, width, height):
        return 2 * (length * width + width * height + height * length)

    @staticmethod
    def calculate_volume(length, width, height):
        return length * width * height
