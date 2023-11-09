import streamlit as st
import pandas as pd
from pycaret.regression import load_model, predict_model

@st.cache_data
def get_tips_model():
    return load_model('tips-best')


st.title('Tips dataset으로 머신러닝 시작하기')

ko = {
    'sex': {'Male': '남성', 'Female': '여성'},
    'smoker': {'Yes': '흡연', 'No': '비흡연'},
    'time': {'Lunch': '점심', 'Dinner': '저녁'},
    'day': {'Sun': '일', 'Sat': '토', 'Fri': '금', 'Thur': '목'}
}

tab1, tab2 = st.tabs(['팁 예측하기', '데이터셋 개요'])

with tab1:
    st.subheader('Tip 예측하기')

    with st.form('팁 금액 예측'):
        total_bill = st.number_input('식사 금액(달러)', min_value=1.00, max_value=1000.00, value=10.00, step=1.0)
        sex = st.selectbox('성별', ko['sex'].keys(), format_func=lambda x: ko['sex'][x])
        smoker = st.selectbox('흡연 여부', ko['smoker'].keys(), format_func=lambda x: ko['smoker'][x])
        time = st.selectbox('식사 시간', ko['time'].keys(), format_func=lambda x: ko['time'][x])
        day = st.selectbox('요일', ko['day'].keys(), format_func=lambda x: ko['day'][x])
        size = st.number_input('식사 인원', min_value=1, max_value=6, value=2, step=1)

        submitted = st.form_submit_button('팁 예측하기')
        if submitted:
            loaded_pipeline = get_tips_model()

            infer_data = pd.DataFrame({'total_bill': [total_bill],
                         'sex': [sex],
                         'smoker': [smoker],
                         'day': [day],
                         'time': [time],
                         'size': [size]
                        })
            with st.spinner('예측 중입니다...'):
                predict_result = predict_model(loaded_pipeline, data=infer_data)
            st.toast(f"예측 완료! :smile: ${predict_result.at[0, 'prediction_label']}")

            st.write(f"예상 팁 금액은 ${predict_result.at[0, 'prediction_label']} 입니다.")



with tab2:
    st.subheader('데이터셋 개요')
    st.write('https://www.kaggle.com/code/sanjanabasu/tips-dataset/input')
    st.write('이 데이터셋은 레스토랑에서 팁을 지불한 손님들의 정보를 담고 있습니다.')

    df = pd.read_csv('tips.csv')

    st.write('학습한 데이터셋은 아래와 같습니다.')
    st.dataframe(df)