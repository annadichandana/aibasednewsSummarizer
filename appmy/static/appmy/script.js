document.getElementById('queryForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const query = document.getElementById('userQuery').value;
    const response = await fetch('/get_summary/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query })
    });

    const data = await response.json();
    displayResult(data);
});

function displayResult(data) {
    const resultContainer = document.getElementById('resultContainer');
    resultContainer.innerHTML = '';

    if (data.error) {
        resultContainer.innerHTML = `<p>${data.error}</p>`;
    } else {
        const summary = data.summary;
        const redirectLink = data.redirect_link;

        resultContainer.innerHTML = `
            <p><strong>Answer:</strong> ${summary}</p>
            <a href="${redirectLink}" target="_blank">Click here for more details</a>
        `;
    }
}
fetch('/your-url/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken  // Add the CSRF token if it's a POST request
    },
    body: JSON.stringify(data)
});
