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

function toggleSection(id) {
  const content = document.getElementById(id);
  const allContents = document.querySelectorAll('.section-content');
  
  // Close all others
  allContents.forEach(el => {
    if (el.id !== id) {
      el.classList.remove('active');
    }
  });
  
  // Toggle current
  content.classList.toggle('active');
}