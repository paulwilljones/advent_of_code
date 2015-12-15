
class Day2Solution(object):

    def calculate_area(self, length, width, height):

        try:
            surface_area_1 = length * width
            surface_area_2 = width * height
            surface_area_3 = height * length
        except ValueError, TypeError:
            print "Values are not integers"
            raise

        return (2 * surface_area_1) + (2 * surface_area_2) + \
               (2 * surface_area_3) + \
               min(surface_area_1, surface_area_2, surface_area_3)