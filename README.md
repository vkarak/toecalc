# toecalc

A simple command-line toe angle to distance converter.

## Usage

### Convert from toe distance to angle

```bash
./toecalc.py d=-1.0 195/55/15
```

```
Toe information:
    Tire size: 195/55/15
    Toe (dist): -1.00mm
    Toe (angle): -0.19° (0°12΄)
```

- Distance argument is in `mm`.


### Convert from toe angle to distance

```bash
./toecalc.py a=-0.1 195/55/15
```

```
Toe information:
    Tire size: 195/55/15
    Toe (dist): -0.52mm
    Toe (angle): -0.10° (0°06΄)
```

- Angle argument may be either in decimal format as above or in `dd:mm` as in the following example:

```bash
./toecalc.py a=-0:10 195/55/15
```

```
Toe information:
    Tire size: 195/55/15
    Toe (dist): -0.87mm
    Toe (angle): -0.17° (0°10΄)
```

- Positive values denote toe-in, negative values denote toe-out
- Units are in metric system only
