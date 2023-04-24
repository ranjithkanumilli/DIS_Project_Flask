//Carousel for trending movies
const carouselContainer = document.querySelector('.carousel-container');
const prevButton = document.querySelector('.prev-button');
const nextButton = document.querySelector('.next-button');
let scrollAmount = 0;
const itemsInView = 5;
const viewWidth = carouselContainer.offsetWidth / itemsInView;
let data = [];

nextButton.addEventListener('click', () => {
  scrollAmount += viewWidth;
  if (scrollAmount > carouselContainer.scrollWidth - viewWidth) {
    scrollAmount = carouselContainer.scrollWidth - viewWidth;
  }
  carouselContainer.scrollTo({
    top: 0,
    left: scrollAmount,
    behavior: 'smooth'
  });
});


prevButton.addEventListener('click', () => {
  scrollAmount -= viewWidth;
  if (scrollAmount < 0) {
    scrollAmount = 0;
  }
  carouselContainer.scrollTo({
    top: 0,
    left: scrollAmount,
    behavior: 'smooth'
  });
});




//Carousel for trending TV
const carouselContainerTv = document.querySelector('.carousel-container-tv');
const prevButtonTv = document.querySelector('.prev-button-tv');
const nextButtonTv = document.querySelector('.next-button-tv');
let scrollAmountTv = 0;
const itemsInViewTv = 5;
const viewWidthTv = carouselContainerTv.offsetWidth / itemsInView;
let dataTv = [];

nextButtonTv.addEventListener('click', () => {
  scrollAmountTv += viewWidthTv;
  if (scrollAmountTv > carouselContainerTv.scrollWidthTv - viewWidthTv) {
    scrollAmountTv = carouselContainerTv.scrollWidthTv - viewWidthTv;
  }
  carouselContainerTv.scrollTo({
    top: 0,
    left: scrollAmountTv,
    behavior: 'smooth'
  });
});


prevButtonTv.addEventListener('click', () => {
  scrollAmountTv -= viewWidthTv;
  if (scrollAmountTv < 0) {
    scrollAmountTv = 0;
  }
  carouselContainerTv.scrollTo({
    top: 0,
    left: scrollAmountTv,
    behavior: 'smooth'
  });
});





const form = document.getElementById('form');
const search = document.getElementById('search');

form.addEventListener('submit', (e) => {
  e.preventDefault();
  const searchTerm = search.value;

  if (searchTerm) {

    window.location.href = `/movies?search=${searchTerm}`;
  }
})

const searchIcon = document.querySelector('.search-icon');
const searchInput = document.querySelector('#search');

searchIcon.addEventListener('click', () => {
  searchInput.focus();
});



// carousel hero - home page

const carousel = document.querySelector(".carousel-hero");
const carouselContainerhero = document.querySelector(".carousel-container-hero");
const prevBtn = document.querySelector(".carousel-hero-prev");
const nextBtn = document.querySelector(".carousel-hero-next");

let currentIndex = 0;
let intervalId;


// Function to go to a specific slide
function goToSlide(index) {
  carouselContainerhero.style.transform = `translateX(-${index * carousel.offsetWidth}px)`;
  currentIndex = index;
}

// Function to go to the next slide
function goToNextSlide() {
  if (currentIndex === carouselContainerhero.children.length - 1) {
    goToSlide(0);
  } else {
    goToSlide(currentIndex + 1);
  }
}

// Function to go to the previous slide
function goToPrevSlide() {
  if (currentIndex === 0) {
    goToSlide(carouselContainerhero.children.length - 1);
  } else {
    goToSlide(currentIndex - 1);
  }
}

// Resize carousel items on window resize
window.addEventListener("resize", () => {
  resizeCarouselItems();
  goToSlide(currentIndex);
});

// Handle previous and next button clicks
prevBtn.addEventListener("click", () => {
  goToPrevSlide();
  clearInterval(intervalId);
});

nextBtn.addEventListener("click", () => {
  goToNextSlide();
  clearInterval(intervalId);
});

// Automatically transition to the next slide every 5 seconds
intervalId = setInterval(() => {
  goToNextSlide();
}, 5000);










