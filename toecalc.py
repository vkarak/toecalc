#!/usr/bin/env python3

import math
import functools
import sys


printout = functools.partial(print, file=sys.stdout)
printerr = functools.partial(print, file=sys.stderr)


class Tire:
    def __init__(self, width, profile, rim):
        self.width = int(width)
        self.profile = int(profile)
        self.rim = int(rim)

    @property
    def diameter(self):
        return 2*self.width*self.profile/100. + self.rim*25.4

    @property
    def radius(self):
        return self.diameter / 2.

    def __repr__(self):
        return 'Tire(%s, %s, %s)' % (self.width, self.profile, self.rim)

    def __str__(self):
        return '%s/%s/%s' % (self.width, self.profile, self.rim)


def calc_toe_angle(toe_dist, radius):
    return math.degrees(math.atan(toe_dist/radius))


def calc_toe_dist(toe_angle, radius):
    return radius * math.tan(math.radians(toe_angle))


def usage():
    printout('Usage: %s {d|a}=TOE TIRE_SIZE' % sys.argv[0])
    printout('   Example: %s d=-1.0 195/55/15' % sys.argv[0])
    printout('   Example: %s a=-0:06 195/55/15' % sys.argv[0])
    printout('   Example: %s a=-0.1 195/55/15' % sys.argv[0])


if __name__ == '__main__':
    try:
        if sys.argv[1] == '-h':
            usage()
            sys.exit(0)
    except IndexError:
        pass

    if len(sys.argv) < 3:
        printerr('%s: too few arguments' % sys.argv[0])
        usage()
        sys.exit(1)

    toe_arg = sys.argv[1]
    try:
        kind, value = toe_arg.split('=')
    except ValueError:
        printerr('%s: could not parse toe argument: %s' %
                 (sys.argv[0], toe_arg))
        sys.exit(1)

    # Parse toe argument
    toe_dist = None
    toe_angle = None
    if kind == 'd':
        try:
            toe_dist = float(value)
        except ValueError:
            printerr('%s: could not parse toe argument: %s' %
                     (sys.argv[0], toe_arg))
            sys.exit(1)
    elif kind == 'a':
        toe_deg, *fraction = value.split(':', maxsplit=1)
        if fraction:
            try:
                fraction = int(fraction[0], base=10)/60.
                if fraction < 0:
                    raise ValueError

                toe_angle = int(toe_deg)
                if toe_angle < 0:
                    toe_angle -= fraction
                elif toe_angle > 0:
                    toe_angle += fraction
                else:
                    toe_angle = -fraction if toe_deg[0] == '-' else fraction

            except ValueError:
                printerr('%s: could not parse toe argument: %s' %
                         (sys.argv[0], toe_arg))
                sys.exit(1)
        else:
            try:
                toe_angle = float(toe_deg)
            except ValueError:
                printerr('%s: could not parse toe argument: %s' %
                         (sys.argv[0], toe_arg))
                sys.exit(1)

    # Parse tire size argument
    try:
        tire_arg = sys.argv[2]
        tire = Tire(*tire_arg.split('/', maxsplit=2))
    except ValueError:
        printerr('%s: could not parse tire size argument: %s' %
                 (sys.argv[0], tire_arg))
        sys.exit(1)

    if toe_dist:
        toe_angle = calc_toe_angle(toe_dist, tire.radius)
    elif toe_angle:
        toe_dist = calc_toe_dist(toe_angle, tire.radius)

    printout('Toe information:')
    printout('    Tire size:', tire)
    printout('    Toe (dist): %.2fmm' % toe_dist)
    printout('    Toe (angle): %.2f° (%d°%d΄)' % (
        toe_angle, int(toe_angle), round((toe_angle - int(toe_angle))*60., 2))
    )
    sys.exit(0)
