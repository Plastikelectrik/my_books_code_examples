wrapped = st.builds(
    lambda v, k: str(v + k * 2**32),
    st.integers(-2, 8), st.integers(-3, 3))
strengths = st.one_of(
    st.integers(-10**12, 10**12).map(str),
    st.text(alphabet="0123456789+- x", max_size=12),
    wrapped,
)
