document.getElementById("fetch-btn").addEventListener("click", () => {
    const home = document.getElementById("home").value || "TeamA";
    const away = document.getElementById("away").value || "TeamB";

    fetch(`https://futbol-tahmin-twuk.onrender.com`)
        .then(res => res.json())
        .then(data => {
            document.getElementById("result").textContent = JSON.stringify(data, null, 2);
        })
        .catch(err => console.error(err));
});
