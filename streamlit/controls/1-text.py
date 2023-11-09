import streamlit as st

st.write('''# st.write()로 쓰면 대충 다 됩니다.
## 이것은 Header
### SubHeader
그냥 텍스트
''')

# 가로줄
st.divider()

# 타이틀
st.title('이것은 타이틀입니다')

# emoji: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.header('이것은 헤더입니다. 이모지도 넣을 수 있어요. 스마일 :smile:')
st.subheader('subheader 입니다. :sunglasses:')
st.markdown('이모지 목록은 https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/ 여기를 참고하세요.')

# 캡션
st.caption('캡션을 넣을 수 있습니다. 캡션은 작은 글씨로 표시됩니다.')

# 코드 표시
sample_code = '''
# python sample code
def function():
    print('hello, world')
'''
st.code(sample_code, language="python")

# 일반 텍스트
st.text('일반적인 텍스트를 입력해 보았습니다.')

# 가로줄
st.divider()

# 마크다운 문법 지원
st.markdown('streamlit은 **마크다운 문법을 지원**합니다.')
# 지원 color : blue, green, orange, red, violet, gray/grey, rainbow
st.markdown("텍스트의 색상을 :green[초록색]으로, 그리고 **:blue[파란색]** 볼트체로 설정할 수 있습니다.")
st.markdown('지원 색상은 :blue[파란색], :green[초록색], :orange[주황색], :red[빨강색], :violet[보라색], :gray[회색], :rainbow[무지개색] 입니다.')
st.markdown(":green[$\sqrt{x^2+y^2}=1$] 와 같이 latex 문법의 수식 표현도 가능합니다 :pencil:")

