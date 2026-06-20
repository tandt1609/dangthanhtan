// Custom interactive behaviors for T&T Personal Hub

document.addEventListener('DOMContentLoaded', () => {
    console.log('%c🚀 T&T Personal Hub initialized successfully!', 'color: #6366f1; font-size: 14px; font-weight: bold;');

    // Add entry animation delays to project cards
    const cards = document.querySelectorAll('.project-card');
    cards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'all 0.6s cubic-bezier(0.16, 1, 0.3, 1)';
        
        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, 150 + index * 100);
    });

    // Add click event tracing to project links
    const projectLinks = document.querySelectorAll('.project-link');
    projectLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            const projectTitle = link.closest('.project-card').querySelector('.project-title').textContent;
            console.log(`🔗 Navigating to project: ${projectTitle}`);
        });
    });
});
