def rag_prompt(question, hits):
    lines = [f"[{i + 1}] ({name}) {text}"
             for i, (name, text) in enumerate(hits)]
    return ("Answer the question using only the\n"
            "sources below. Cite sources like [1].\n"
            "If the sources do not contain the answer,\n"
            "say that you do not know.\n\n"
            "Sources:\n" + "\n".join(lines) +
            f"\n\nQuestion: {question}")

hits = [("router.txt", "Hold the reset button "
         "for two seconds.")]
print(rag_prompt("How do I restart the router?", hits))
