import os
import shlex
import subprocess

from hypothesis import given, settings
from hypothesis import strategies as st

ORIGINAL = shlex.split(os.environ["KETTLE_ORIGINAL"])
REBUILD = shlex.split(os.environ["KETTLE_REBUILD"])

teas = st.sampled_from(["green", "black", "oolong",
                        "herbal", "mint"])
strengths = st.one_of(
    st.integers(-10**12, 10**12).map(str),
    st.text(alphabet="0123456789+- x", max_size=12),
)


def run(cmd, args):
    p = subprocess.run(cmd + args, capture_output=True,
                       text=True, timeout=5)
    return p.returncode, p.stdout


@settings(max_examples=300, deadline=None)
@given(teas, strengths)
def test_same_behavior(tea, strength):
    args = [tea, strength]
    assert run(ORIGINAL, args) == run(REBUILD, args)
