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

document.querySelectorAll('.btn').forEach(btn => {
    btn.addEventListener('click', function(e) {
    e.preventDefault();
    alert('Registration page will open here!');
    });
});

const ctx = document.getElementById('isesChart').getContext('2d');
    new Chart(ctx, {
      type: 'doughnut',
      data: {
        labels: [
          'USA (10%)',
          'Germany (10%)',
          'UK/Sweden/Switzerland (6%)',
          'India (8%)',
          'Norway (6%)',
          'China (6%)',
          'Australia (6%)',
          'Spain (3%)',
          'Brazil (2%)',
          'Other countries (39%)'
        ],
        datasets: [{
          data: [10, 10, 6, 8, 6, 6, 6, 3, 2, 39],
          backgroundColor: [
            '#FF6384', // USA
            '#36A2EB', // Germany
            '#FFCE56', // UK/Sweden/Switzerland
            '#4BC0C0', // India
            '#9966FF', // Norway
            '#FF9F40', // China
            '#7B68EE', // Australia
            '#2E8B57', // Spain
            '#DAA520', // Brazil
            '#CCCCCC'  // Other countries
          ],
          borderWidth: 1,
          borderColor: '#fff'
        }]
      },
      options: {
        responsive: true,
        plugins: {
          legend: {
            position: 'right',
            align: 'start',
            labels: {
              boxWidth: 15,
              padding: 10,
              font: {
                size: 12
              }
            }
          },
          tooltip: {
            callbacks: {
              label: function(context) {
                return `${context.label}: ${context.raw}%`;
              }
            }
          }
        },
        layout: {
          padding: 10
        }
      }
    });