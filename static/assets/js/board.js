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

function showBio(slug) {
  document.querySelectorAll('.bio-card').forEach(card => {
    card.classList.remove('active');
  });
  // Tanlangan biografiyani ko'rsatish
  const card = document.getElementById('bio-' + slug);
  if (card) {
    card.classList.add('active');
  }
}

function hideBio(slug) {
  const card = document.getElementById('bio-' + slug);
  if (card) {
    card.classList.remove('active');
  }
}