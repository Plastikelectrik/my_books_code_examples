# SPEC: kettle 1.0 (stripped build)

## 1. Scope
In scope: command-line behavior, output, exit codes.
Out of scope: performance, memory layout.
Target: kettle-stripped, SHA-256 in INDEX.md.

## 2. Interface
Usage: kettle TEA [STRENGTH]
Output: one line on standard output.
Exit codes: 0 ok, 1 usage, 2 strength, 3 tea.

## 3. Requirements
REQ-001 (SEEN) With no TEA argument, print the
  usage line and exit with status 1.
  Evidence: F-01, observations. Test: T-001.
REQ-002 (SEEN) STRENGTH defaults to 3.
  Evidence: F-05, ev_62d, Frida capture 2.
REQ-003 (SEEN) STRENGTH is parsed as a decimal
  integer; text without leading digits is 0.
  Evidence: observations (abc). Test: T-003.
REQ-004 (SEEN) If STRENGTH < 1 or > 5, print the
  strength error line, exit 2. Test: T-004.
REQ-005 (SEEN) Teas are matched exactly against
  the table in section 4, in table order.
  Evidence: ev_51c, Frida strcmp capture.
REQ-006 (SEEN) Unknown tea: print the unknown-tea
  line with the given name, exit 3. Test: T-006.
REQ-007 (SEEN) time = base + (strength - 3) * 20.
REQ-008 (SEEN) If temp < 85: time += (85-temp)*2.
REQ-009 (SEEN) If time < 30: time = 30.
REQ-010 (SEEN) check = H(name) mod 10007, where
  H starts at 7 and, for each byte b of the name,
  H = (H * 31 + b) mod 2^32.
REQ-011 (SEEN) Success line format:
  "<tea> <temp>C <time>s check=<check>", exit 0.

## 4. Data
| tea    | temp C | base s |
| green  | 80     | 120    |
| black  | 95     | 240    |
| oolong | 90     | 180    |
| herbal | 100    | 300    |

## 6. Open questions (INFERRED)
Q-001 Behavior of STRENGTH values with leading
  digits and trailing text, such as "4x".

## 7. Known limits (UNKNOWN)
U-001 Behavior for TEA longer than 4096 bytes.
U-002 Behavior when standard output is closed.
