// Filtrado de la sección "Proyectos"
// Botones en `#filters` usan `data-filter`; items usan `data-category`.
function setupProjectFilters() {
  const filterButtons = document.querySelectorAll('#filters .filter-btn');
  const projectItems = document.querySelectorAll('#proyectos [data-category]');

  if (!filterButtons.length || !projectItems.length) return;

  filterButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const filter = btn.getAttribute('data-filter');

      // Actualizar clase activa en botones
      filterButtons.forEach(b => b.classList.remove('active', 'bg-blue-600', 'text-white'));
      btn.classList.add('active', 'bg-blue-600', 'text-white');

      // Mostrar/ocultar items
      projectItems.forEach(item => {
        const cat = item.getAttribute('data-category');
        if (filter === 'all' || cat === filter) {
          item.classList.remove('hidden');
        } else {
          item.classList.add('hidden');
        }
      });
    });
  });
}

// Navegación suave con scroll
document.addEventListener('DOMContentLoaded', function() {
  // Configurar tabs del header
  const tabButtons = document.querySelectorAll('.tab-btn');

  // Click en botones de la cabecera (desktop)
  tabButtons.forEach(button => {
    button.addEventListener('click', function() {
      const targetId = this.dataset.tab;
      const targetSection = document.getElementById(targetId);

      if (targetSection) {
        // Quitar activo de todos
        tabButtons.forEach(btn => {
          btn.classList.remove('border-blue-600', 'text-blue-600');
          btn.classList.add('border-transparent');
        });

        // Agregar activo a este
        this.classList.remove('border-transparent');
        this.classList.add('border-blue-600', 'text-blue-600');

        // Scroll suave a la sección (compensa header fijo)
        const headerOffset = document.querySelector('header') ? document.querySelector('header').offsetHeight : 0;
        const elementPosition = targetSection.getBoundingClientRect().top + window.scrollY;
        const offsetPosition = elementPosition - headerOffset - 10;

        window.scrollTo({ top: offsetPosition, behavior: 'smooth' });
      }
    });
  });

  // Detectar sección visible para activar tab (usa secciones con id)
  const sections = document.querySelectorAll('section[id]');

  window.addEventListener('scroll', function() {
    let current = '';

    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      if (window.scrollY >= (sectionTop - 160)) {
        current = section.id;
      }
    });

    // Actualizar tab activo
    if (current) {
      tabButtons.forEach(btn => {
        btn.classList.remove('border-blue-600', 'text-blue-600');
        btn.classList.add('border-transparent');

        if (btn.dataset.tab === current) {
          btn.classList.remove('border-transparent');
          btn.classList.add('border-blue-600', 'text-blue-600');
        }
      });
    }
  });

  // Funciones para el menú mobile y navegación desde móvil
  window.toggleMenu = function() {
    const menu = document.getElementById('mobileMenu');
    if (!menu) return;
    menu.classList.toggle('hidden');
  }

  window.showTab = function(tabId) {
    const target = document.getElementById(tabId);
    if (!target) return;
    const headerOffset = document.querySelector('header') ? document.querySelector('header').offsetHeight : 0;
    const elementPosition = target.getBoundingClientRect().top + window.scrollY;
    const offsetPosition = elementPosition - headerOffset - 10;
    window.scrollTo({ top: offsetPosition, behavior: 'smooth' });
  }

  // Inicializar filtros de proyectos
  try { setupProjectFilters(); } catch (e) { /* no hacer nada si no existe la sección */ }
});
