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
            .catch(error => {
                // Silently fail in production
                if (process.env.NODE_ENV !== 'production') console.error('Error loading metadata:', error);
            });
    }

    // Render notebook items in terminal style
    function renderNotebooks(notebooks) {
        notebooksContainer.innerHTML = '';
        
        if (notebooks.length === 0) {
            noResults.classList.add('show');
            return;
        }
        
        noResults.classList.remove('show');
        
        notebooks.forEach((notebook, index) => {
            const item = document.createElement('a');
            item.href = notebook.url || `${notebook.id}.html`;
            item.className = 'notebook-item fade-in';
            item.style.animationDelay = `${index * 0.05}s`;
            
            item.innerHTML = `
                <div class="notebook-title">${notebook.title}</div>
                <div class="notebook-desc">${notebook.description}</div>
                <div class="notebook-path">${notebook.url || `${notebook.id}.html`}</div>
            `;
            
            notebooksContainer.appendChild(item);
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

    // Clear search on Escape key
    searchInput.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            searchInput.value = '';
            filterNotebooks('');
        }
    });

    // Load notebooks on page load
    loadNotebooks();
});

