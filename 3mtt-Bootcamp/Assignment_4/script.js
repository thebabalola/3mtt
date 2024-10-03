const startBtn = document.getElementById('startBtn');
const countdownDisplay = document.getElementById('countdown');
let countdownInterval;

startBtn.addEventListener('click', function () {
    const inputTime = document.getElementById('timeInput').value;
    let timeRemaining = parseInt(inputTime);

    if (isNaN(timeRemaining) || timeRemaining <= 0) {
        alert('Please enter a valid number of seconds.');
        return;
    }

    clearInterval(countdownInterval);  // Clear any previous countdown

    countdownInterval = setInterval(function () {
        const minutes = Math.floor(timeRemaining / 60);
        const seconds = timeRemaining % 60;

        countdownDisplay.textContent = `${formatTime(minutes)}:${formatTime(seconds)}`;

        if (timeRemaining <= 0) {
            clearInterval(countdownInterval);
            countdownDisplay.textContent = "Thank You!";
        }

        timeRemaining--;
    }, 1000);
});

function formatTime(time) {
    return time < 10 ? `0${time}` : time;
}
