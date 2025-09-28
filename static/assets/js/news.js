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

document.addEventListener('DOMContentLoaded', function () {
  const pageLinks = document.querySelectorAll('.page-link');
  const prevBtn = document.getElementById('prevBtn');
  const nextBtn = document.getElementById('nextBtn');
  const firstBtn = document.getElementById('firstBtn');
  const lastBtn = document.getElementById('lastBtn');

  // Sahifalar soni (statik — yoki dinamik olish mumkin)
  const totalPages = document.querySelectorAll('.page-link').length;
  let currentPage = 1;

  // Faol sahifani belgilash
  function setActivePage(page) {
    currentPage = page;
    pageLinks.forEach(link => {
      const pageNum = parseInt(link.getAttribute('data-page'));
      if (pageNum === page) {
        link.style.fontWeight = 'bold';
        link.style.color = '#ff0000';
      } else {
        link.style.fontWeight = 'normal';
        link.style.color = '';
      }
    });
    // Bu yerda sahifa kontentini yangilash kerak (masalan, yangiliklarni)
    console.log('Sahifa:', currentPage);
  }

  // Dastlab 1-sahifa faol
  setActivePage(1);

  // Sahifa tugmalariga bosish
  pageLinks.forEach(link => {
    link.addEventListener('click', function (e) {
      e.preventDefault();
      const page = parseInt(this.getAttribute('data-page'));
      setActivePage(page);
    });
  });

  // First
  firstBtn.addEventListener('click', function (e) {
    e.preventDefault();
    setActivePage(1);
  });

  // Last
  lastBtn.addEventListener('click', function (e) {
    e.preventDefault();
    setActivePage(totalPages);
  });

  // Previous
  prevBtn.addEventListener('click', function (e) {
    e.preventDefault();
    if (currentPage > 1) {
      setActivePage(currentPage - 1);
    }
  });

  // Next
  nextBtn.addEventListener('click', function (e) {
    e.preventDefault();
    if (currentPage < totalPages) {
      setActivePage(currentPage + 1);
    }
  });
});