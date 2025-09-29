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

const bios = {
  'viktoria-martin': `
    <strong>Prof. Viktoria Martin</strong> is Professor in Energy Technology at KTH Royal Institute of Technology in Stockholm, Sweden. A graduate from KTH (MSc in Chemical Engineering 1993) and the University of Florida (PhD in Mechanical Engineering 1998), she has pursued a career in international research collaborations with the International Energy Agency as well as the EU, providing insight into a variety of leading research and education arenas. Dr. Martin has over 25 years of experience in education, research, and entrepreneurship in the area of sustainable energy, with special focus on energy systems analysis, sector-coupling, and thermal energy storage. She is the author/co-author of 100+ publications within her research area. Equally important to her work on high quality education within the field, and she is presently the director of an engineering BSc degree programme in Energy and Environment, and teaches master level courses in sustainable energy systems.
  `,
  'andreas-hauer': `
    <strong>Dr. Andreas Hauer</strong> is a leading expert in energy storage and smart grids. He has led numerous EU-funded projects and serves on several international advisory boards. As Vice President, he supports the President in governance and strategic planning.
  `,
  'chiel-boonstra': `
    <strong>Mr. Chiel Boonstra</strong> brings extensive financial expertise to ISES. With a background in corporate finance and non-profit management, he ensures the society's financial health and sustainability.
  `,
  'michael-leung': `
    <strong>Prof. Michael Leung</strong> is an expert in photovoltaic materials and system integration. He coordinates internal communications and external relations for ISES, ensuring smooth operations and stakeholder engagement.
  `,
  'aline-kirsten': `
    <strong>Dr. Aline Kirsten Vidal de Oliveira</strong> focuses on solar policy and education. She leads initiatives to engage young professionals and students in solar energy, fostering the next generation of leaders.
  `,
  'gurleen-kaur': `
    <strong>Dr. Gurleen Kaur</strong> represents the voice of young professionals in ISES. She advocates for youth inclusion in decision-making and promotes innovative approaches to solar energy adoption.
  `,
  'klaus-vajen': `
    <strong>Prof. Klaus Vajen</strong> has served ISES in multiple leadership roles. His legacy includes expanding the society's global reach and strengthening partnerships with academic and industry stakeholders.
  `,
  'andreas-haeberle': `
    <strong>Dr. Andreas Häberle</strong> is a pioneer in solar architecture and building-integrated photovoltaics. He has contributed significantly to the development of solar standards and guidelines.
  `,
  'david-renne': `
    <strong>Dr. David Renné</strong> is an expert in solar resource assessment and climate modeling. He has worked with international agencies to improve solar data accessibility and accuracy.
  `,
  'christine-lins': `
    <strong>Christine Lins</strong> is a globally recognized leader in renewable energy policy and advocacy. She has played a key role in shaping international climate agreements and promoting solar energy deployment.
  `,
  'geoff-stapleton': `
    <strong>Geoff Stapleton</strong> has decades of experience in solar industry development and project financing. He advises governments and private sector on scaling up solar energy investments.
  `,
  'genene-mola': `
    <strong>Prof. Genene Tessema Mola</strong> is a leading researcher in solar energy applications in Africa. She champions regional cooperation and capacity building for sustainable energy transitions.
  `,
  'francisco-beltran': `
    <strong>Francisco Beltran</strong> represents the interests of young professionals in ISES. He organizes events and workshops to foster knowledge exchange and career development in the solar sector.
  `,
  'berta-garcia': `
    <strong>Prof. Berta García Fernández</strong> specializes in solar energy economics and market design. She works with policymakers to create enabling environments for solar energy investment.
  `,
  'jianhua-fan': `
    <strong>Dr. Jianhua Fan</strong> is a senior executive in a major solar technology company. He bridges the gap between industry innovation and academic research, driving practical solar solutions.
  `,
  'ashvini-kumar': `
    <strong>Dr Ashvini Kumar</strong> is an expert in solar energy policy and regulation. He has advised multiple governments on designing effective solar energy frameworks and incentive programs.
  `,
  'andreas-kazantzidis': `
    <strong>Andreas Kazantzidis</strong> is a renowned scientist in atmospheric solar radiation and climate modeling. His research informs solar energy forecasting and system optimization.
  `,
  'saman-gunasekara': `
    <strong>Dr. Saman Nimai Gunasekara</strong> focuses on solar energy integration in developing economies. He works on off-grid and mini-grid solar solutions to improve energy access.
  `,
  'oluwatoyn-ogedengbe': `
    <strong>Oluwatoyn Ogedengbe</strong> is a passionate advocate for gender equality in the solar energy sector. She leads initiatives to empower women and underrepresented groups in renewable energy careers.
  `
};

// Biografiyani ko'rsatish
function showBio(id) {
  const modal = document.getElementById('bio-modal');
  const title = document.getElementById('modal-title');
  const body = document.getElementById('modal-body');

  if (bios[id]) {
    title.textContent = id.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
    body.innerHTML = bios[id];
    modal.style.display = 'flex';
  }
}

// Biografiyani yopish
function closeBio() {
  document.getElementById('bio-modal').style.display = 'none';
}

// Ekranga bosilganda ham yopish
window.onclick = function(event) {
  const modal = document.getElementById('bio-modal');
  if (event.target === modal) {
    closeBio();
  }
};