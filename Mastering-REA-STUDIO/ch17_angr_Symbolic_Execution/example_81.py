import sys
import angr

try:
    import claripy
except ImportError:
    from angr import claripy

path = sys.argv[1]
proj = angr.Project(path, auto_load_libs=False)
code = claripy.BVS("code", 8 * 8)
state = proj.factory.entry_state(args=[path, code])
for byte in code.chop(8):
    state.solver.add(byte >= ord("a"))
    state.solver.add(byte <= ord("z"))

sim = proj.factory.simulation_manager(state)
sim.explore(
    find=lambda s: b"OPEN" in s.posix.dumps(1),
    avoid=lambda s: b"LOCKED" in s.posix.dumps(1),
)
if sim.found:
    found = sim.found[0]
    print(found.solver.eval(code, cast_to=bytes))
else:
    print("no solution found")
