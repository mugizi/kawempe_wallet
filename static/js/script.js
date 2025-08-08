document.addEventListener('DOMContentLoaded', function() {
    const inputs = document.querySelectorAll('input');
    inputs.forEach(function(el) {
        el.addEventListener('focus', function() {
            el.style.borderColor = '#007bff';
        });
        el.addEventListener('blur', function() {
            el.style.borderColor = '#ccc';
        });
    });
});
