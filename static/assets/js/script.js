// === Dropdown Toggle ===
function toggleDropdown(id) {
  const dropdowns = document.querySelectorAll('.mega-menu1, .mega-menu2, .mega-menu3');
  dropdowns.forEach(drop => {
    if (drop.id === id) {
      drop.style.display = drop.style.display === 'block' ? 'none' : 'block';
    } else {
      drop.style.display = 'none';
    }
  });
}

// Tashqariga bosilganda yopish
document.addEventListener('click', function (e) {
    if (!e.target.closest('.navbar li')) {
        document.querySelectorAll('.mega-menu1, .mega-menu2, .mega-menu3')
        .forEach(drop => drop.style.display = 'none');
  }
});

// === Marquee control ===
document.addEventListener("DOMContentLoaded", function () {
  const marquee = document.querySelector(".marquee-text");
  let isPaused = false;

    function setSpeed(speed) {
        if (marquee) {
            marquee.style.animationDuration = speed + "s";
        }
    }

function togglePause() {
    if (!marquee) return;
    if (isPaused) {
      marquee.style.animationPlayState = "running";
      isPaused = false;
    } else {
      marquee.style.animationPlayState = "paused";
      isPaused = true;
    }
}

setSpeed(15); // boshlang‘ich tezlik
});

// === Cards hover effect ===
document.querySelectorAll('.card').forEach(card => {
    card.addEventListener('mouseenter', () => {
        card.style.transform = 'translateY(-5px)';
        card.style.boxShadow = '0 10px 20px rgba(0, 0, 0, 0.3)';
  });

    card.addEventListener('mouseleave', () => {
        card.style.transform = 'translateY(0)';
        card.style.boxShadow = 'none';
  });
});

// === Hero section update on card click ===
document.addEventListener("DOMContentLoaded", function () {
    const cards = document.querySelectorAll('.card');
    const heroImg = document.getElementById('hero-img');
    const heroTitle = document.getElementById('hero-title');
    const heroLink = document.getElementById('hero-link');
    const heroType = document.getElementById('hero-type');

    cards.forEach(card => {
        card.addEventListener('click', function () {
            const imgSrc = this.getAttribute('data-img');
            const title = this.getAttribute('data-title');
            const type = this.getAttribute('data-type');
            const linkText = this.getAttribute('data-link');

    if (heroImg && heroTitle && heroLink && heroType) {
        heroImg.src = imgSrc;
        heroTitle.textContent = title;
        heroLink.textContent = linkText;
        heroType.textContent = type;

        heroImg.style.opacity = '0';
        heroTitle.style.opacity = '0';
        heroLink.style.opacity = '0';
        heroType.style.opacity = '0';

        setTimeout(() => {
            heroImg.style.opacity = '1';
            heroTitle.style.opacity = '1';
            heroLink.style.opacity = '1';
            heroType.style.opacity = '1';
            }, 100);
        }
        });
    });
});

const searchBox = document.getElementById('searchBox');
const toggle = document.getElementById('searchToggle');
const input = searchBox.querySelector('.search-input');

toggle.addEventListener('click', () => {
  searchBox.classList.toggle('active');
  if (searchBox.classList.contains('active')) {
    input.focus();
  }
});

// ESC bosganda yopilsin
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && searchBox.classList.contains('active')) {
    searchBox.classList.remove('active');
    input.value = '';
  }
});

function scrollCarousel(carouselId, direction) {
  const carousel = document.getElementById(carouselId);
  const itemWidth = carousel.querySelector('.carousel-item').offsetWidth + 20; // + gap
  const currentScroll = carousel.scrollLeft;
  const newScroll = currentScroll + (itemWidth * direction);

  carousel.scrollTo({
    left: newScroll,
    behavior: 'smooth'
  });

  // Avtomatikni to'xtatish (agar kerak bo'lsa)
  if (direction !== 0) {
    stopAutoScroll(carouselId);
  }
}

// Avtomatik siljish uchun
let autoIntervals = {};

function startAutoScroll(carouselId) {
  const carousel = document.getElementById(carouselId);
  const itemWidth = carousel.querySelector('.carousel-item').offsetWidth + 20;

  autoIntervals[carouselId] = setInterval(() => {
    const currentScroll = carousel.scrollLeft;
    const maxScroll = carousel.scrollWidth - carousel.clientWidth;

    if (currentScroll >= maxScroll) {
      carousel.scrollTo({ left: 0, behavior: 'smooth' });
    } else {
      carousel.scrollTo({
        left: currentScroll + itemWidth,
        behavior: 'smooth'
      });
    }
  }, 5000); // Har 5 soniyada
}

function stopAutoScroll(carouselId) {
  if (autoIntervals[carouselId]) {
    clearInterval(autoIntervals[carouselId]);
    delete autoIntervals[carouselId];
  }
}

// Sliderlarni avtomatik ishga tushirish
document.addEventListener('DOMContentLoaded', () => {
  // Boshlang'ich holatda avtomatik ishga tushirish
  startAutoScroll('members-carousel');
  startAutoScroll('partners-carousel');

  // Foydalanuvchi tugmalarga bosganda avtomatikni to'xtatish
  document.querySelectorAll('.carousel-arrow').forEach(button => {
    button.addEventListener('click', () => {
      const carouselId = button.parentElement.querySelector('.carousel').id;
      stopAutoScroll(carouselId);
    });
  });

  // Slider ustiga sichqoncha kelsa — to'xtatish
  document.querySelectorAll('.carousel-container').forEach(container => {
    container.addEventListener('mouseenter', () => {
      const carouselId = container.querySelector('.carousel').id;
      stopAutoScroll(carouselId);
    });
    container.addEventListener('mouseleave', () => {
      const carouselId = container.querySelector('.carousel').id;
      startAutoScroll(carouselId);
    });
  });
});