// constants.js
const appendTailwindCSS = () => {
    const link = document.createElement("link");
    link.href = "https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css";
    link.rel = "stylesheet";
    document.head.appendChild(link);
};

// Call the function to append the Tailwind CSS link
appendTailwindCSS();
