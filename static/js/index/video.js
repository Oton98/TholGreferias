document.addEventListener("DOMContentLoaded", function() {
    const video = document.getElementById("videoThol");

    function startPreview() {
      video.muted = true;
      video.currentTime = 1;
      video.playbackRate = 1; 
      video.loop = true;
      video.play();
    }

    function stopPreview() {
      video.currentTime = 0;
      video.playbackRate = 1;
      video.pause();
    }

    function handleIntersection(entries, observer) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          startPreview();
        } else {
          stopPreview();
        }
      });
    }

    const observerOptions = {
      root: null,
      rootMargin: "0px",
      threshold: 0.2
    };

    const observer = new IntersectionObserver(handleIntersection, observerOptions);

    observer.observe(video.parentElement); // Observa el contenedor del video, no el video directamente
  });