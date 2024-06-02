import streamlit as st

def auto_check(number_adult, number_child):
    
    madori_recommend=[]
    if number_adult == 1 and number_child == 0:
        st.session_state.checkbox_states['one_room'] = True
        st.session_state.checkbox_states['one_DK_LDK'] = True
        st.session_state.checkbox_states['two_DK_LDK'] = False
        st.session_state.checkbox_states['three_DK_LDK'] = False
        st.session_state.checkbox_states['four_DK_LDK'] = False
        madori_recommend.extend(['1R', '1K', '1DK', '1LDK'])
    
    if number_adult == 2 and number_child == 0:
        st.session_state.checkbox_states['one_room'] = False
        st.session_state.checkbox_states['one_DK_LDK'] = True
        st.session_state.checkbox_states['two_DK_LDK'] = True
        st.session_state.checkbox_states['three_DK_LDK'] = False
        st.session_state.checkbox_states['four_DK_LDK'] = False
        madori_recommend.extend(['1DK', '1LDK', '2K', '2DK', '2LDK'])

    if number_adult == 3 and number_child == 0:
        st.session_state.checkbox_states['one_room'] = False
        st.session_state.checkbox_states['one_DK_LDK'] = False
        st.session_state.checkbox_states['two_DK_LDK'] = True
        st.session_state.checkbox_states['three_DK_LDK'] = True
        st.session_state.checkbox_states['four_DK_LDK'] = False
        madori_recommend.extend(['2K', '2DK', '2LDK', '3K', '3DK', '3LDK'])

    if number_adult == 4 and number_child == 0:
        st.session_state.checkbox_states['one_room'] = False
        st.session_state.checkbox_states['one_DK_LDK'] = False
        st.session_state.checkbox_states['two_DK_LDK'] = True
        st.session_state.checkbox_states['three_DK_LDK'] = True
        st.session_state.checkbox_states['four_DK_LDK'] = False
        madori_recommend.extend(['2K', '2DK', '2LDK', '3K', '3DK', '3LDK'])

    if number_adult == 2 and number_child == 1:
        st.session_state.checkbox_states['one_room'] = False
        st.session_state.checkbox_states['one_DK_LDK'] = True
        st.session_state.checkbox_states['two_DK_LDK'] = True
        st.session_state.checkbox_states['three_DK_LDK'] = False
        st.session_state.checkbox_states['four_DK_LDK'] = False
        madori_recommend.extend(['1K', '1DK', '1LDK', '2K', '2DK', '2LDK'])

    if number_adult == 2 and number_child == 1:
        st.session_state.checkbox_states['one_room'] = False
        st.session_state.checkbox_states['one_DK_LDK'] = True
        st.session_state.checkbox_states['two_DK_LDK'] = True
        st.session_state.checkbox_states['three_DK_LDK'] = False
        st.session_state.checkbox_states['four_DK_LDK'] = False
        madori_recommend.extend(['1K', '1DK', '1LDK', '2K', '2DK', '2LDK'])

    if number_adult == 3 and number_child == 1:
        st.session_state.checkbox_states['one_room'] = False
        st.session_state.checkbox_states['one_DK_LDK'] = False
        st.session_state.checkbox_states['two_DK_LDK'] = False
        st.session_state.checkbox_states['three_DK_LDK'] = True
        st.session_state.checkbox_states['four_DK_LDK'] = True
        madori_recommend.extend(['3K', '3DK', '3LDK', '4K', '4DK', '4LDK'])

    if number_adult == 4 and number_child == 1:
        st.session_state.checkbox_states['one_room'] = False
        st.session_state.checkbox_states['one_DK_LDK'] = False
        st.session_state.checkbox_states['two_DK_LDK'] = False
        st.session_state.checkbox_states['three_DK_LDK'] = True
        st.session_state.checkbox_states['four_DK_LDK'] = True
        madori_recommend.extend(['3K', '3DK', '3LDK', '4K', '4DK', '4LDK'])        

    if number_adult == 1 and number_child == 2:
        st.session_state.checkbox_states['one_room'] = False
        st.session_state.checkbox_states['one_DK_LDK'] = False
        st.session_state.checkbox_states['two_DK_LDK'] = True
        st.session_state.checkbox_states['three_DK_LDK'] = True
        st.session_state.checkbox_states['four_DK_LDK'] = False
        madori_recommend.extend(['2K', '2DK', '2LDK', '3K', '3DK', '3LDK'])

    if number_adult == 2 and number_child == 2:
        st.session_state.checkbox_states['one_room'] = False
        st.session_state.checkbox_states['one_DK_LDK'] = False
        st.session_state.checkbox_states['two_DK_LDK'] = True
        st.session_state.checkbox_states['three_DK_LDK'] = True
        st.session_state.checkbox_states['four_DK_LDK'] = False
        madori_recommend.extend(['2K', '2DK', '2LDK', '3K', '3DK', '3LDK'])

    if number_adult == 3 and number_child == 2:
        st.session_state.checkbox_states['one_room'] = False
        st.session_state.checkbox_states['one_DK_LDK'] = False
        st.session_state.checkbox_states['two_DK_LDK'] = False
        st.session_state.checkbox_states['three_DK_LDK'] = True
        st.session_state.checkbox_states['four_DK_LDK'] = True
        madori_recommend.extend(['3K', '3DK', '3LDK', '4K', '4DK', '4LDK'])

    if number_adult == 4 and number_child == 2:
        st.session_state.checkbox_states['one_room'] = False
        st.session_state.checkbox_states['one_DK_LDK'] = False
        st.session_state.checkbox_states['two_DK_LDK'] = False
        st.session_state.checkbox_states['three_DK_LDK'] = True
        st.session_state.checkbox_states['four_DK_LDK'] = True
        madori_recommend.extend(['3K', '3DK', '3LDK', '4K', '4DK', '4LDK'])

    if number_child == 3:
        st.session_state.checkbox_states['one_room'] = False
        st.session_state.checkbox_states['one_DK_LDK'] = False
        st.session_state.checkbox_states['two_DK_LDK'] = False
        st.session_state.checkbox_states['three_DK_LDK'] = True
        st.session_state.checkbox_states['four_DK_LDK'] = True
        madori_recommend.extend(['3K', '3DK', '3LDK', '4K', '4DK', '4LDK'])
    
    print("おすすめの間取り:",madori_recommend)

    return madori_recommend