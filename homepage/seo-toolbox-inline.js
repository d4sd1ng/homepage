(() => {
  const frame = document.getElementById("nv-seo-inline-frame");
  if (!frame) return;
  const source = new URL(frame.src);
  window.addEventListener("message", (event) => {
    if (event.origin !== source.origin || event.source !== frame.contentWindow) return;
    const data = event.data;
    if (!data || data.type !== "nv-seo-height" || !Number.isFinite(data.height)) return;
    if (data.height < 100 || data.height > 3000) return;
    frame.style.height = `${Math.ceil(data.height)}px`;
  });
  if (new URLSearchParams(location.search).get("owner") === "1") {
    source.searchParams.set("owner", "1");
    frame.src = source.href;
    frame.parentElement.scrollIntoView();
  }
})();
