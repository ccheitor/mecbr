const toggle = document.querySelector("[data-nav-toggle]");
const nav = document.querySelector("[data-nav]");

if (toggle && nav) {
  toggle.addEventListener("click", () => {
    nav.classList.toggle("open");
  });
}

const heroVideo = document.querySelector(".hero-video");

if (heroVideo) {
  heroVideo.muted = true;
  heroVideo.defaultMuted = true;
  heroVideo.setAttribute("playsinline", "");

  const playHeroVideo = () => {
    const promise = heroVideo.play();
    if (promise !== undefined) {
      promise.catch(() => {
        heroVideo.addEventListener(
          "click",
          () => {
            heroVideo.play();
          },
          { once: true }
        );
      });
    }
  };

  if (heroVideo.readyState >= 2) {
    playHeroVideo();
  } else {
    heroVideo.addEventListener("loadeddata", playHeroVideo, { once: true });
  }
}

const reveals = document.querySelectorAll(".reveal");

if ("IntersectionObserver" in window) {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.16, rootMargin: "0px 0px -40px 0px" }
  );

  reveals.forEach((el) => observer.observe(el));
} else {
  reveals.forEach((el) => el.classList.add("is-visible"));
}
