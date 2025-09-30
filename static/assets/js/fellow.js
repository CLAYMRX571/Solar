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

// Har bir rasm uchun alohida indeks saqlash
const imageIndices = {
  img1: 0,
  img2: 0,
  img3: 0
};

// Rasmlar ro'yxati (har bir konteyner uchun)
const imageLists = {
  img1: [
    "static/assets/img/fullstack.jpg",
  ],
  img2: [
    "static/assets/img/fullstack.jpg",
  ],
  img3: [
    "static/assets/img/fullstack.jpg",
  ]
};

function nextImage(containerId) {
  const container = document.getElementById(containerId);
  const img = container.querySelector('img');
  let index = imageIndices[containerId];
  index = (index + 1) % imageLists[containerId].length;
  imageIndices[containerId] = index;
  img.src = imageLists[containerId][index];
}

function prevImage(containerId) {
  const container = document.getElementById(containerId);
  const img = container.querySelector('img');
  let index = imageIndices[containerId];
  index = (index - 1 + imageLists[containerId].length) % imageLists[containerId].length;
  imageIndices[containerId] = index;
  img.src = imageLists[containerId][index];
}

function closeImage(btn) {
  const container = btn.closest('.image-container');
  alert("Rasm yopildi. Haqiqiy dasturda bu yerda modal yoki element o'chiriladi.");
  // Masalan: container.style.display = 'none';
}