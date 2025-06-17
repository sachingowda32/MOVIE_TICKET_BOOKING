// otp-timer.js
let time = 600; // 10 minutes in seconds
const timerElement = document.getElementById('timer');

const countdown = setInterval(() => {
    let minutes = Math.floor(time / 60);
    let seconds = time % 60;

    minutes = minutes < 10 ? '0' + minutes : minutes;
    seconds = seconds < 10 ? '0' + seconds : seconds;

    timerElement.textContent = `${minutes}:${seconds}`;

    if (time <= 0) {
        clearInterval(countdown);
        timerElement.textContent = "OTP expired!";
        document.querySelectorAll(".otp-inputs input").forEach(input => input.disabled = true);
    }

    time--;
}, 1000);
