function playVideo() {
    var video = document.querySelector("video");
    video.play();
}

function pauseVideo() {
    var video = document.querySelector("video");
    video.pause();
}

function toggleSidebar() {
    var sidebar = document.querySelector(".sidebar");
    sidebar.classList.toggle("active");

    if (sidebar.classList.contains("active")) {
        botao.innerHTML = "X";
    }
    else {
        botao.innerHTML ="☰";
    }
}