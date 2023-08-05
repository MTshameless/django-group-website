const slides = document.querySelector(".slides");
let slideIndex = 0;

function showSlide() {
  const slideWidth = document.querySelector(".carousel").offsetWidth;
  slides.style.transform = `translateX(-${slideWidth * slideIndex}px)`;

  // Update the active dot
  const dots = document.querySelectorAll(".dot");
  dots.forEach((dot, index) => {
    dot.classList.toggle("active-dot", index === slideIndex);
  });
}

function nextSlide() {
  slideIndex++;
  if (slideIndex >= slides.children.length) {
    slideIndex = 0;
  }
  showSlide();
}

function prevSlide() {
  slideIndex--;
  if (slideIndex < 0) {
    slideIndex = slides.children.length - 1;
  }
  showSlide();
}

function currentSlide(index) {
  slideIndex = index - 1;
  showSlide();
}

// Automatic slide change every 5 seconds
setInterval(nextSlide, 5000);

// Optional: Add event listeners for next and previous buttons
const nextButton = document.querySelector(".next-button");
const prevButton = document.querySelector(".prev-button");

nextButton.addEventListener("click", nextSlide);
prevButton.addEventListener("click", prevSlide);
