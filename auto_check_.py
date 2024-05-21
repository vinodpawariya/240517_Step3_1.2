import streamlit as st

def auto_check(number_adult, number_child):
    

    if number_adult == 1 and number_child == 0:
        st.session_state.checkbox_states['one_room'] = True
        st.session_state.checkbox_states['one_DK_LDK'] = True
        st.session_state.checkbox_states['two_DK_LDK'] = False
        st.session_state.checkbox_states['three_DK_LDK'] = False
        st.session_state.checkbox_states['four_DK_LDK'] = False

    if number_adult == 2 and number_child == 0:
        st.session_state.checkbox_states['one_room'] = False
        st.session_state.checkbox_states['one_DK_LDK'] = True
        st.session_state.checkbox_states['two_DK_LDK'] = True
        st.session_state.checkbox_states['three_DK_LDK'] = False
        st.session_state.checkbox_states['four_DK_LDK'] = False

    if number_adult == 3 and number_child == 0:
        st.session_state.checkbox_states['one_room'] = False
        st.session_state.checkbox_states['one_DK_LDK'] = False
        st.session_state.checkbox_states['two_DK_LDK'] = True
        st.session_state.checkbox_states['three_DK_LDK'] = True
        st.session_state.checkbox_states['four_DK_LDK'] = False

    if number_adult == 4 and number_child == 0:
        st.session_state.checkbox_states['one_room'] = False
        st.session_state.checkbox_states['one_DK_LDK'] = False
        st.session_state.checkbox_states['two_DK_LDK'] = True
        st.session_state.checkbox_states['three_DK_LDK'] = True
        st.session_state.checkbox_states['four_DK_LDK'] = False

    if number_adult == 2 and number_child == 1:
        st.session_state.checkbox_states['one_room'] = False
        st.session_state.checkbox_states['one_DK_LDK'] = True
        st.session_state.checkbox_states['two_DK_LDK'] = True
        st.session_state.checkbox_states['three_DK_LDK'] = False
        st.session_state.checkbox_states['four_DK_LDK'] = False

    if number_adult == 2 and number_child == 1:
        st.session_state.checkbox_states['one_room'] = False
        st.session_state.checkbox_states['one_DK_LDK'] = True
        st.session_state.checkbox_states['two_DK_LDK'] = True
        st.session_state.checkbox_states['three_DK_LDK'] = False
        st.session_state.checkbox_states['four_DK_LDK'] = False

    if number_adult == 3 and number_child == 1:
        st.session_state.checkbox_states['one_room'] = False
        st.session_state.checkbox_states['one_DK_LDK'] = False
        st.session_state.checkbox_states['two_DK_LDK'] = False
        st.session_state.checkbox_states['three_DK_LDK'] = True
        st.session_state.checkbox_states['four_DK_LDK'] = True

    if number_adult == 4 and number_child == 1:
        st.session_state.checkbox_states['one_room'] = False
        st.session_state.checkbox_states['one_DK_LDK'] = False
        st.session_state.checkbox_states['two_DK_LDK'] = False
        st.session_state.checkbox_states['three_DK_LDK'] = True
        st.session_state.checkbox_states['four_DK_LDK'] = True

    if number_adult == 1 and number_child == 2:
        st.session_state.checkbox_states['one_room'] = False
        st.session_state.checkbox_states['one_DK_LDK'] = False
        st.session_state.checkbox_states['two_DK_LDK'] = True
        st.session_state.checkbox_states['three_DK_LDK'] = True
        st.session_state.checkbox_states['four_DK_LDK'] = False

    if number_adult == 2 and number_child == 2:
        st.session_state.checkbox_states['one_room'] = False
        st.session_state.checkbox_states['one_DK_LDK'] = False
        st.session_state.checkbox_states['two_DK_LDK'] = True
        st.session_state.checkbox_states['three_DK_LDK'] = True
        st.session_state.checkbox_states['four_DK_LDK'] = False

    if number_adult == 3 and number_child == 2:
        st.session_state.checkbox_states['one_room'] = False
        st.session_state.checkbox_states['one_DK_LDK'] = False
        st.session_state.checkbox_states['two_DK_LDK'] = False
        st.session_state.checkbox_states['three_DK_LDK'] = True
        st.session_state.checkbox_states['four_DK_LDK'] = True

    if number_adult == 4 and number_child == 2:
        st.session_state.checkbox_states['one_room'] = False
        st.session_state.checkbox_states['one_DK_LDK'] = False
        st.session_state.checkbox_states['two_DK_LDK'] = False
        st.session_state.checkbox_states['three_DK_LDK'] = True
        st.session_state.checkbox_states['four_DK_LDK'] = True

    if number_child == 3:
        st.session_state.checkbox_states['one_room'] = False
        st.session_state.checkbox_states['one_DK_LDK'] = False
        st.session_state.checkbox_states['two_DK_LDK'] = False
        st.session_state.checkbox_states['three_DK_LDK'] = True
        st.session_state.checkbox_states['four_DK_LDK'] = True