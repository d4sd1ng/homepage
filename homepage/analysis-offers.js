(() => {
  document.querySelectorAll("[data-analysis-offer]").forEach(card => {
    const stage = card.querySelector(".nv-analyse__stage");
    const detailsElements = [...stage.querySelectorAll(".nv-analyse__disclosure")];
    const controls = [...stage.querySelectorAll("[data-action]")];
    const images = [...stage.querySelectorAll(".nv-analyse__image-block")];
    let revision = 0;

    const getOpenDetails = () => detailsElements.findIndex(details => details.open);

    const syncState = async () => {
      const currentRevision = ++revision;
      const currentIndex = getOpenDetails();
      const hasOpenDetails = currentIndex !== -1;
      images.forEach((image, index) => image.classList.toggle("is-active", index === currentIndex + 1));
      controls.forEach(button => { button.hidden = !hasOpenDetails; });
      if (!hasOpenDetails) {
        stage.dataset.checkingDetails = "false";
        return;
      }
      const animations = stage.getAnimations({ subtree: true }).filter(animation =>
        animation.effect.getComputedTiming().iterations !== Infinity
      );
      await Promise.allSettled(animations.map(animation => animation.finished));
      if (currentRevision === revision) {
        stage.dataset.checkingDetails = String(getOpenDetails() !== -1);
      }
    };

    const navigate = direction => {
      const currentIndex = getOpenDetails();
      if (currentIndex === -1) return;
      detailsElements[currentIndex].open = false;
      const nextIndex = (currentIndex + direction + detailsElements.length) % detailsElements.length;
      detailsElements[nextIndex].open = true;
    };

    const close = () => {
      const currentIndex = getOpenDetails();
      if (currentIndex === -1) return;
      detailsElements[currentIndex].open = false;
      detailsElements[currentIndex].querySelector("summary").focus();
    };

    stage.querySelector('[data-action="next"]').addEventListener("click", () => navigate(1));
    stage.querySelector('[data-action="previous"]').addEventListener("click", () => navigate(-1));
    stage.querySelector('[data-action="exit"]').addEventListener("click", close);
    stage.addEventListener("keydown", event => {
      if (event.key !== "Escape" || getOpenDetails() === -1) return;
      event.preventDefault();
      close();
    });
    stage.addEventListener("toggle", syncState, true);
    syncState();
  });
})();
