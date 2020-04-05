// This particular file handles all the animation that occurs on the various pages!
const date = new Date();
const newDate = date.toUTCString();
const date_element = document.getElementById('date').innerHTML = newDate;

const btn = document.getElementById('btn');

btn.addEventListener('click', () => {
    alert("welcome");
})