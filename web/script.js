(function () {
  "use strict";

  // —— Timeline ——
  var slider = document.getElementById("timeline-slider");
  var yearEl = document.getElementById("timeline-year");
  var fillEl = document.getElementById("timeline-fill");
  var contentEl = document.getElementById("timeline-content");

  var eraCopy = {
    early: "Construction and early years. The community gathers. Nickels, dimes, and dreams.",
    mid1: "Open-air masses, growth, and faith through hardship.",
    mid2: "Restoration and renewal. Children fill the school.",
    late: "New generations. Stories passed down.",
    now: "Today: children's drawings, letters to 2125, and the living parish."
  };

  if (slider && yearEl && fillEl && contentEl) {
    function getEra(value) {
      if (value < 1920) return eraCopy.early;
      if (value < 1950) return eraCopy.mid1;
      if (value < 1980) return eraCopy.mid2;
      if (value < 2010) return eraCopy.late;
      return eraCopy.now;
    }
    function updateTimeline() {
      var min = 1905;
      var max = 2025;
      var value = Number(slider.value);
      var pct = ((value - min) / (max - min)) * 100;
      yearEl.textContent = value;
      fillEl.style.width = pct + "%";
      var caption = contentEl.querySelector(".timeline-caption");
      if (caption) caption.textContent = getEra(value);
    }
    slider.addEventListener("input", updateTimeline);
    updateTimeline();
  }

  // —— Map: open modal with story ——
  var modal = document.getElementById("modal");
  var modalTitle = document.getElementById("modal-title");
  var modalBody = document.getElementById("modal-body");
  var modalClose = document.getElementById("modal-close");

  var placeStories = {
    church: {
      title: "The Church",
      body: "This is where we gather. Kids drew the stained glass and wrote what faith means to them. Scan the QR in the book to hear a child read their letter to the next 100 years."
    },
    school: {
      title: "The School",
      body: "Generations learned here. Tap Memory Walk when you're on site to open the drawing gallery and hear students explain the cornerstone."
    },
    heritage: {
      title: "Heritage Center",
      body: "Archives and oral history live here. Grandma's stories, retold by children—click through the timeline to see how the parish changed over the years."
    },
    olive: {
      title: "Olive Street",
      body: "The heart of the parish. Walk the street with your phone for GPS-triggered stories at each spot."
    }
  };

  function openModal(place) {
    var story = placeStories[place];
    if (!story || !modal || !modalTitle || !modalBody) return;
    modalTitle.textContent = story.title;
    modalBody.textContent = story.body;
    modal.setAttribute("aria-hidden", "false");
    modal.classList.add("is-open");
    document.body.style.overflow = "hidden";
    modalClose.focus();
  }

  function closeModal() {
    if (!modal) return;
    modal.classList.remove("is-open");
    modal.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
  }

  if (modalClose) modalClose.addEventListener("click", closeModal);
  if (modal) {
    modal.addEventListener("click", function (e) {
      if (e.target === modal) closeModal();
    });
  }
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && modal && modal.classList.contains("is-open")) closeModal();
  });

  var buildings = document.querySelectorAll(".map-building");
  buildings.forEach(function (el) {
    el.addEventListener("click", function () {
      var place = el.getAttribute("data-place");
      if (place && placeStories[place]) openModal(place);
    });
  });

  // —— Scroll reveal ——
  var sections = document.querySelectorAll(".section");
  var observer = typeof IntersectionObserver !== "undefined"
    ? new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) entry.target.classList.add("reveal");
          });
        },
        { rootMargin: "0px 0px -80px 0px", threshold: 0.1 }
      )
    : null;

  if (observer) {
    sections.forEach(function (s) {
      observer.observe(s);
    });
  } else {
    sections.forEach(function (s) {
      s.classList.add("reveal");
    });
  }
})();
