// Script to render notebooks and handle search functionality

document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const notebooksContainer = document.getElementById('notebooksContainer');
    const noResults = document.getElementById('noResults');
    
    let allNotebooks = [];

    // Fetch metadata and render notebooks
    function loadNotebooks() {
        fetch('metadata.json')
            .then(response => response.json())
            .then(data => {
                allNotebooks = Object.entries(data.notebooks).map(([key, value]) => ({
                    id: key,
                    ...value
                }));
                renderNotebooks(allNotebooks);
            })
            .catch(error => console.error('Error loading metadata:', error));
    }

    // Render notebook cards
    function renderNotebooks(notebooks) {
        notebooksContainer.innerHTML = '';
        
        if (notebooks.length === 0) {
            noResults.classList.remove('hidden');
            return;
        }
        
        noResults.classList.add('hidden');
        
        notebooks.forEach((notebook, index) => {
            const card = document.createElement('a');
            card.href = `${notebook.id}.html`;
            card.className = 'block fade-in';
            card.style.animationDelay = `${index * 0.1}s`;
            
            card.innerHTML = `
                <div class="bg-slate-700 hover:bg-slate-600 rounded-lg p-6 h-full cursor-pointer transition-all duration-300 group border border-slate-600 hover:border-blue-500">
                    <div class="text-4xl mb-3">${notebook.icon || '📚'}</div>
                    <h3 class="text-lg font-semibold text-white mb-2 group-hover:text-blue-400 transition">
                        ${notebook.title}
                    </h3>
                    <p class="text-gray-300 text-sm leading-relaxed mb-4">
                        ${notebook.description}
                    </p>
                    <span class="inline-block text-blue-400 text-sm font-medium group-hover:text-blue-300 transition">
                        Open notebook →
                    </span>
                </div>
            `;
            
            notebooksContainer.appendChild(card);
        });
    }

    // Search functionality
    function filterNotebooks(searchTerm) {
        const term = searchTerm.toLowerCase();
        
        const filtered = allNotebooks.filter(notebook => 
            notebook.title.toLowerCase().includes(term) ||
            notebook.description.toLowerCase().includes(term) ||
            notebook.id.toLowerCase().includes(term)
        );
        
        renderNotebooks(filtered);
    }

    // Event listener for search input
    searchInput.addEventListener('input', (e) => {
        filterNotebooks(e.target.value);
    });

    // Load notebooks on page load
    loadNotebooks();
});
