import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="streamlit + HTML Clock 🐰", layout="centered")

st.markdown("""
    <style>
        body, .stApp {
            background-color: #fce4ec;
            color: #6a1b9a;
            font-family: 'Comic Sans MS', cursive;
            text-align: center;
        }
        .title {
            font-size: 32px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .subtitle {
            font-size: 20px;
            margin-top: 5px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🎀 Kawaii Round Clock ⏰</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Every second is cuter than the last 💕</div>', unsafe_allow_html=True)

html_code = """
<div style="display: flex; justify-content: center; align-items: center; margin-top: 30px;">
  <div class="clock">
    <!-- Clock Numbers -->
    <div class="number number1">1</div>
    <div class="number number2">2</div>
    <div class="number number3">3</div>
    <div class="number number4">4</div>
    <div class="number number5">5</div>
    <div class="number number6">6</div>
    <div class="number number7">7</div>
    <div class="number number8">8</div>
    <div class="number number9">9</div>
    <div class="number number10">10</div>
    <div class="number number11">11</div>
    <div class="number number12">12</div>

    <!-- Clock Hands -->
    <div class="hand hour" id="hour"></div>
    <div class="hand minute" id="minute"></div>
    <div class="hand second" id="second"></div>
    <div class="center"></div>
  </div>
</div>

<style>
.clock {
  width: 250px;
  height: 250px;
  border: 10px solid #ffc1cc;
  border-radius: 50%;
  position: relative;
  background: #fff0f5;
  box-shadow: 0 0 20px #ffb6c1 inset;
}

.hand {
  position: absolute;
  bottom: 50%;
  left: 50%;
  transform-origin: bottom;
  transform: rotate(90deg);
  background: #fff;
  border-radius: 2px;
}

.hour {
  width: 6px;
  height: 60px;
  z-index: 3;
}

.minute {
  width: 4px;
  height: 90px;
  z-index: 2;
}

.second {
  width: 2px;
  height: 100px;
  background: #e75480;
  z-index: 1;
}

.center {
  width: 14px;
  height: 14px;
  background: #e75480;
  border-radius: 50%;
  position: absolute;
  top: 50%;
  left: 50%;
  margin: -7px 0 0 -7px;
  z-index: 5;
}

.number {
  position: absolute;
  width: 30px;
  height: 30px;
  text-align: center;
  line-height: 30px;
  color: #e75480;
  font-weight: bold;
  font-family: 'Comic Sans MS', cursive;
  font-size: 16px;
  pointer-events: none;
}

.number1  { top: 18px;  left: 165px; }
.number2  { top: 45px;  left: 200px; }
.number3  { top: 110px; left: 220px; }
.number4  { top: 175px; left: 200px; }
.number5  { top: 210px; left: 165px; }
.number6  { top: 225px; left: 110px; }
.number7  { top: 210px; left: 50px; }
.number8  { top: 175px; left: 15px; }
.number9  { top: 110px; left: 0px; }
.number10 { top: 45px;  left: 15px; }
.number11 { top: 18px;  left: 50px; }
.number12 { top: 0px;   left: 110px; }
</style>

<script>
function updateClock() {
    const now = new Date();
    const sec = now.getSeconds();
    const min = now.getMinutes();
    const hr  = now.getHours();

    const secDeg = sec * 6;
    const minDeg = min * 6 + sec * 0.1;
    const hrDeg  = ((hr % 12) / 12) * 360 + (min / 60) * 30;

    document.getElementById("second").style.transform = `rotate(${secDeg}deg)`;
    document.getElementById("minute").style.transform = `rotate(${minDeg}deg)`;
    document.getElementById("hour").style.transform = `rotate(${hrDeg}deg)`;
}

setInterval(updateClock, 1000);
updateClock();
</script>
"""

components.html(html_code, height=400)
