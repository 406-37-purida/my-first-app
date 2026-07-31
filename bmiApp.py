import streamlit as st
st.mardown("# :red[แอปพลิเคชั่นคำนวณค่าดัชนีมวลกาย BMI]")
st.write("กรอกข้อมูลน้ำหนักและส่วนสูงของคุณ เพื่อเช็กสุขภาพเบื่องต้น")

weight = st.number_input("กรอกน้ำหนักของคุณ (กิโลกรัม):")
height_cm = st.number_input("กรอกส่วนสูงของคุณ (เซนติเมตร):")

if st.button("คำนวณค่า BMI")
    height_m = height_cm / 100
    bmi = weight / (height_m **2)

    st.write("---")
    st.header(f"ค่า BMI ของคุณคือ: **{bmi:.2f}**")

if bmi < 18.5:
    st.warning("คุณมีน้ำหนักน้อยกว่าเกณฑ์ (ผอม)")
elif 18.5 <= bmi < 25.0:
    st.success("คุณมีน้ำหักอยู่ในเกณฑ์ปกติ (สุขภาพดี)")
elif 23.0 <= bmi < 25.0:
    st.info("คุรเริ่มมีน้ำหนัเกินเกณฑ์ (ท้วม)")
else:
    st.error("คุณอยู่ในเกณฑ์อ้วน ควรระวังเรื่องสุขภาพและการออกกำลังกาย")

st.divider()
st.write("นางสาวปูริดา สอนศิริ เลขที่ 37 ม.4/6")
