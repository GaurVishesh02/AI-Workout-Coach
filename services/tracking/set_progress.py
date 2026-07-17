import time
import streamlit as st
from services.persistence.exercise_repository import add_exercise

def update_set_progress():
    reps_per_set = st.session_state.get("reps_per_set", 0)
    target_sets = st.session_state.get("target_sets", 0)
    total_reps = st.session_state.get("reps", 0)
    exercise = st.session_state.get("exercise_type")
    user_id = st.session_state.get("user_id")

    if not reps_per_set or reps_per_set <= 0:
        return

    sets_completed = total_reps // reps_per_set
    current_set_reps = total_reps % reps_per_set

    if target_sets and sets_completed >= target_sets:
        sets_completed = target_sets
        current_set_reps = 0
        st.session_state["workout_complete"] = True

    st.session_state["sets_completed"] = sets_completed
    st.session_state["current_set_reps"] = current_set_reps

    # Naye complete hue sets ko DB me save karo
    last_saved = st.session_state.get("last_saved_sets_completed", 0)
    if sets_completed > last_saved and user_id and exercise:
        newly_completed = sets_completed - last_saved
        elapsed = int(time.time() - st.session_state.get("set_cycle_started_at", time.time()))

        add_exercise(
            user_id,
            exercise,
            reps_per_set * newly_completed,
            newly_completed,
            elapsed
        )

        st.session_state["last_saved_sets_completed"] = sets_completed
        st.session_state["set_cycle_started_at"] = time.time()