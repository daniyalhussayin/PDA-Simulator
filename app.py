
import streamlit as st
import pandas as pd
from pda_simulator import (
    simulate_anbn,
    simulate_palindrome_wcwr
)

st.set_page_config(page_title="PDA Language Identifier", layout="centered")
st.title("🧠 PDA Language Identifier")

language = st.selectbox("Select a Language Pattern", [
    "L = { aⁿ bⁿ | n ≥ 1 }",
    "L = { w c wᴿ | w ∈ {a, b}* }"
])

user_input = st.text_input("Enter a string to simulate:")

if st.button("🧪 Run PDA Simulation"):
    if not user_input:
        st.warning("⚠️ Please enter a string.")
    else:
        if language == "L = { aⁿ bⁿ | n ≥ 1 }":
            accepted, steps, final_state, final_stack = simulate_anbn(user_input)
        elif language == "L = { w c wᴿ | w ∈ {a, b}* }":
            accepted, steps, final_state, final_stack = simulate_palindrome_wcwr(user_input)

        rows = []
        for i, step in enumerate(steps, start=1):
            parts = step.split("|")
            if len(parts) == 5:
                state, symbol, stack_top, new_stack, action = [p.strip() for p in parts]
                rows.append({
                    "Step": i,
                    "State": state,
                    "Symbol": symbol,
                    "Top of Stack": stack_top,
                    "Stack After": new_stack,
                    "Action": action
                })

        if rows:
            st.subheader("📜 PDA Simulation Steps")
            st.table(pd.DataFrame(rows))

        st.markdown("---")
        st.subheader("✅ Final Result")
        st.markdown(f"**Language Pattern:** `{language}`")
        st.markdown(f"**Final State:** `{final_state}`")
        st.markdown(f"**Final Stack:** `{''.join(final_stack)}`")

        if accepted:
            st.success(f"✅ Result: String '{user_input}' is **ACCEPTED** by PDA.")
        else:
            st.error(f"❌ Result: String '{user_input}' is **REJECTED** by PDA.")
