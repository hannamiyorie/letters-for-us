const API_URL = 'http://127.0.0.1:5000/api/messages';

const messageForm = document.getElementById('message-form');
const messagesContainer = document.getElementById('messages-container');

// Fungsi untuk menampilkan semua pesan
async function fetchAndDisplayMessages() {
    try {
        const response = await fetch(API_URL);
        const messages = await response.json();

        messagesContainer.innerHTML = ''; // Kosongkan kontainer dulu

        if (messages.length === 0) {
            messagesContainer.innerHTML = '<p>Belum ada pesan.</p>';
            return;
        }

        messages.forEach(msg => {
            const messageCard = document.createElement('div');
            messageCard.className = 'message-card';
            messageCard.innerHTML = `
                <p>${msg.content}</p>
                <div class="meta">
                    <strong>Dari: ${msg.name}</strong> - <span>${msg.created_at}</span>
                </div>
            `;
            messagesContainer.appendChild(messageCard);
        });
    } catch (error) {
        console.error('Gagal memuat pesan:', error);
        messagesContainer.innerHTML = '<p>Gagal memuat pesan.</p>';
    }
}

// Fungsi untuk menangani pengiriman form
messageForm.addEventListener('submit', async (event) => {
    event.preventDefault(); // Mencegah form reload halaman

    const nameInput = document.getElementById('name');
    const contentInput = document.getElementById('content');

    const messageData = {
        name: nameInput.value,
        content: contentInput.value
    };

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(messageData),
        });

        if (!response.ok) {
            throw new Error('Gagal mengirim pesan');
        }

        // Kosongkan form dan muat ulang pesan
        nameInput.value = '';
        contentInput.value = '';
        fetchAndDisplayMessages();

    } catch (error) {
        console.error('Error saat mengirim pesan:', error);
        alert('Gagal mengirim pesan.');
    }
});

// Muat pesan saat halaman pertama kali dibuka
fetchAndDisplayMessages();