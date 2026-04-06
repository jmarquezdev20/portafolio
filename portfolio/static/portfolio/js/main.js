/**
 * Portfolio JS Principal
 * Maneja: navbar, animaciones, skills, filtro proyectos, formulario contacto
 */

document.addEventListener('DOMContentLoaded', () => {

  // ────────────────────────────────────────────
  // NAVBAR — sticky + active link
  // ────────────────────────────────────────────
  const navbar = document.getElementById('navbar');
  const navLinks = document.querySelectorAll('.nav-link');
  const sections = document.querySelectorAll('section[id]');

  const updateNavbar = () => {
    if (window.scrollY > 80) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }

    // Highlight active nav link based on scroll position
    let current = '';
    sections.forEach(section => {
      const sectionTop = section.offsetTop - 120;
      if (window.scrollY >= sectionTop) {
        current = section.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === `#${current}`) {
        link.classList.add('active');
      }
    });
  };

  window.addEventListener('scroll', updateNavbar, { passive: true });
  updateNavbar();

  // ────────────────────────────────────────────
  // MOBILE MENU TOGGLE
  // ────────────────────────────────────────────
  const navToggle = document.getElementById('navToggle');
  const navLinksContainer = document.getElementById('navLinks');

  if (navToggle) {
    navToggle.addEventListener('click', () => {
      navLinksContainer.classList.toggle('open');
      // Animate hamburger
      const spans = navToggle.querySelectorAll('span');
      spans.forEach(s => s.style.background = navLinksContainer.classList.contains('open')
        ? 'var(--cyan)' : '');
    });

    // Close on link click
    navLinksContainer.querySelectorAll('.nav-link').forEach(link => {
      link.addEventListener('click', () => {
        navLinksContainer.classList.remove('open');
      });
    });

    // Close on outside click
    document.addEventListener('click', (e) => {
      if (!navToggle.contains(e.target) && !navLinksContainer.contains(e.target)) {
        navLinksContainer.classList.remove('open');
      }
    });
  }

  // ────────────────────────────────────────────
  // SCROLL REVEAL — Intersection Observer
  // ────────────────────────────────────────────
  const revealElements = document.querySelectorAll(
    '.skill-category, .project-card, .timeline-card, .contact-channel, .about-info-card'
  );

  revealElements.forEach(el => el.classList.add('reveal'));

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        // Stagger delay for grid items
        const delay = (Array.from(entry.target.parentElement.children)
          .indexOf(entry.target)) * 80;
        setTimeout(() => {
          entry.target.classList.add('visible');
        }, delay);
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

  revealElements.forEach(el => revealObserver.observe(el));

  // ────────────────────────────────────────────
  // SKILL BARS ANIMATION
  // ────────────────────────────────────────────
  const skillFills = document.querySelectorAll('.skill-fill');

  const skillObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const target = entry.target;
        const width = target.dataset.width;
        setTimeout(() => {
          target.style.width = `${width}%`;
        }, 200);
        skillObserver.unobserve(target);
      }
    });
  }, { threshold: 0.5 });

  skillFills.forEach(fill => skillObserver.observe(fill));

  // ────────────────────────────────────────────
  // PROJECT FILTER
  // ────────────────────────────────────────────
  const filterBtns = document.querySelectorAll('.filter-btn');
  const projectCards = document.querySelectorAll('.project-card');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const filter = btn.dataset.filter;

      // Update active button
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      // Filter cards with animation
      projectCards.forEach((card, i) => {
        const category = card.dataset.category;
        const show = filter === 'all' || category === filter;

        if (show) {
          card.style.display = '';
          setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = '';
          }, i * 50);
        } else {
          card.style.opacity = '0';
          card.style.transform = 'scale(0.95)';
          setTimeout(() => {
            card.style.display = 'none';
          }, 300);
        }
      });
    });
  });

  // ────────────────────────────────────────────
  // CONTACT FORM — AJAX Submission
  // ────────────────────────────────────────────
  const contactForm = document.getElementById('contactForm');
  const submitBtn = document.getElementById('submitBtn');
  const formSuccess = document.getElementById('formSuccess');
  const formError = document.getElementById('formError');

  if (contactForm) {
    contactForm.addEventListener('submit', async (e) => {
      e.preventDefault();

      const btnText = submitBtn.querySelector('.btn-text');
      const btnLoading = submitBtn.querySelector('.btn-loading');

      // Show loading state
      btnText.style.display = 'none';
      btnLoading.style.display = 'inline';
      submitBtn.disabled = true;

      // Hide previous messages
      formSuccess.style.display = 'none';
      formError.style.display = 'none';

      try {
        const formData = new FormData(contactForm);
        const response = await fetch(contactForm.action, {
          method: 'POST',
          body: formData,
          headers: {
            'X-Requested-With': 'XMLHttpRequest',
          }
        });

        const data = await response.json();

        if (data.success) {
          formSuccess.style.display = 'block';
          contactForm.reset();
          // Scroll to success message
          formSuccess.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        } else {
          formError.style.display = 'block';
          // Show field errors if any
          if (data.errors) {
            Object.entries(data.errors).forEach(([field, errors]) => {
              const input = document.getElementById(`id_${field}`);
              if (input) {
                input.style.borderColor = 'var(--rose)';
              }
            });
          }
        }
      } catch (err) {
        formError.style.display = 'block';
        console.error('Contact form error:', err);
      } finally {
        btnText.style.display = 'inline-flex';
        btnLoading.style.display = 'none';
        submitBtn.disabled = false;
      }
    });

    // Reset border color on input focus
    contactForm.querySelectorAll('.form-input').forEach(input => {
      input.addEventListener('focus', () => {
        input.style.borderColor = '';
      });
    });
  }

  // ────────────────────────────────────────────
  // SCROLL TO TOP BUTTON
  // ────────────────────────────────────────────
  const scrollTopBtn = document.getElementById('scrollTop');

  if (scrollTopBtn) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 500) {
        scrollTopBtn.classList.add('visible');
      } else {
        scrollTopBtn.classList.remove('visible');
      }
    }, { passive: true });

    scrollTopBtn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // ────────────────────────────────────────────
  // FOOTER YEAR
  // ────────────────────────────────────────────
  const footerYear = document.getElementById('footerYear');
  if (footerYear) {
    footerYear.textContent = new Date().getFullYear();
  }

  // ────────────────────────────────────────────
  // AUTO-DISMISS DJANGO MESSAGES
  // ────────────────────────────────────────────
  const djangoMessages = document.querySelectorAll('.django-msg');
  djangoMessages.forEach(msg => {
    setTimeout(() => {
      msg.style.opacity = '0';
      msg.style.transform = 'translateX(100%)';
      msg.style.transition = 'all 0.4s ease';
      setTimeout(() => msg.remove(), 400);
    }, 5000);
  });

  // ────────────────────────────────────────────
  // SMOOTH SCROLL for internal links
  // ────────────────────────────────────────────
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
      const target = document.querySelector(anchor.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  console.log('%c Portfolio Django 🐍', 'color: #00D4FF; font-size: 16px; font-weight: bold;');
  console.log('%c Built with Python + Django', 'color: #00E5A0; font-size: 12px;');
});
