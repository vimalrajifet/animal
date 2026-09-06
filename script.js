const ANIMAL_EMOJIS = {
    "antelope": "🦌", "badger": "🦡", "bat": "🦇", "bear": "🐻", "bee": "🐝",
    "beetle": "🪲", "bison": "🦬", "boar": "🐗", "butterfly": "🦋", "cat": "🐱",
    "caterpillar": "🐛", "chimpanzee": "🐵", "cockroach": "🪳", "cow": "🐮", "coyote": "🐺",
    "crab": "🦀", "crow": "🦅", "deer": "🦌", "dog": "🐶", "dolphin": "🐬",
    "donkey": "🫏", "dragonfly": "🦗", "duck": "🦆", "eagle": "🦅", "elephant": "🐘",
    "flamingo": "🦩", "fly": "🪰", "fox": "🦊", "goat": "🐐", "goldfish": "🐟",
    "goose": "🪿", "gorilla": "🦍", "grasshopper": "🦗", "hamster": "🐹", "hare": "🐇",
    "hedgehog": "🦔", "hippopotamus": "🦛", "hornbill": "🦜", "horse": "🐴", "hummingbird": "🐦",
    "hyena": "🐕", "jellyfish": "🪼", "kangaroo": "🦘", "koala": "🐨", "ladybugs": "🐞",
    "leopard": "🐆", "lion": "🦁", "lizard": "🦎", "lobster": "🦞", "mosquito": "🦟",
    "moth": "🦋", "mouse": "🐭", "octopus": "🐙", "okapi": "🦓", "orangutan": "🦧",
    "otter": "🦦", "owl": "🦉", "ox": "🐂", "oyster": "🦪", "panda": "🐼",
    "parrot": "🦜", "pelecaniformes": "🦤", "penguin": "🐧", "pig": "🐷", "pigeon": "🐦",
    "porcupine": "🦔", "possum": "🦝", "raccoon": "🦝", "rat": "🐀", "reindeer": "🦌",
    "rhinoceros": "🦏", "sandpiper": "🐦", "seahorse": "🐡", "seal": "🦭", "shark": "🦈",
    "sheep": "🐑", "snake": "🐍", "sparrow": "🐦", "squid": "🦑", "squirrel": "🐿️",
    "starfish": "⭐", "swan": "🦢", "tiger": "🐅", "turkey": "🦃", "turtle": "🐢",
    "whale": "🐋", "wolf": "🐺", "wombat": "🐻", "woodpecker": "🐦", "zebra": "🦓"
};

// DOM elements
const dropZone = document.getElementById('dropZone');
const fileInput = document.getElementById('fileInput');
const dropPrompt = document.getElementById('dropPrompt');
const previewWrap = document.getElementById('previewWrap');
const imagePreview = document.getElementById('imagePreview');
const removeBtn = document.getElementById('removeBtn');
const loadingStatus = document.getElementById('loadingStatus');
const statusMessage = document.getElementById('statusMessage');
const resultsCard = document.getElementById('resultsCard');

// Prediction UI elements
const tierBadge = document.getElementById('tierBadge');
const confScore = document.getElementById('confScore');
const animalEmoji = document.getElementById('animalEmoji');
const animalName = document.getElementById('animalName');
const tierMessage = document.getElementById('tierMessage');
const top5List = document.getElementById('top5List');

// Facts elements
const animalOverview = document.getElementById('animalOverview');
const specSciName = document.getElementById('specSciName');
const specDiet = document.getElementById('specDiet');
const specHabitat = document.getElementById('specHabitat');
const specStatus = document.getElementById('specStatus');
const specLifespan = document.getElementById('specLifespan');
const funFactText = document.getElementById('funFactText');

// Voice elements
const speakBtn = document.getElementById('speakBtn');
const stopBtn = document.getElementById('stopBtn');
const soundWave = document.getElementById('soundWave');
const voiceStatus = document.getElementById('voiceStatus');
const autoSpeakToggle = document.getElementById('autoSpeakToggle');

let currentSpeechText = "";

// Drag and drop handlers
['dragenter', 'dragover'].forEach(eventName => {
    dropZone.addEventListener(eventName, (e) => {
        e.preventDefault();
        dropZone.classList.add('dragover');
    }, false);
});

['dragleave', 'drop'].forEach(eventName => {
    dropZone.addEventListener(eventName, (e) => {
        e.preventDefault();
        dropZone.classList.remove('dragover');
    }, false);
});

dropZone.addEventListener('drop', (e) => {
    const dt = e.dataTransfer;
    const files = dt.files;
    if (files.length) {
        handleImageFile(files[0]);
    }
});

fileInput.addEventListener('change', (e) => {
    if (e.target.files.length) {
        handleImageFile(e.target.files[0]);
    }
});

removeBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    resetUpload();
});

function resetUpload() {
    stopSpeaking();
    fileInput.value = '';
    imagePreview.src = '';
    previewWrap.classList.add('hidden');
    dropPrompt.classList.remove('hidden');
    resultsCard.classList.add('hidden');
    loadingStatus.classList.add('hidden');
}

function handleImageFile(file) {
    if (!file.type.startsWith('image/')) {
        alert("Please upload a valid image file (JPG, PNG, WEBP).");
        return;
    }

    const reader = new FileReader();
    reader.onload = (e) => {
        imagePreview.src = e.target.result;
        dropPrompt.classList.add('hidden');
        previewWrap.classList.remove('hidden');
    };
    reader.readAsDataURL(file);

    uploadAndPredict(file);
}

const DEFAULT_CLOUD_BACKEND = 'https://animal-vision-vimal.loca.lt';

function getApiEndpoint() {
    const custom = localStorage.getItem('animal_backend_url');
    if (custom) return custom.replace(/\/+$/, '') + '/predict';

    if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
        return '/predict';
    }
    return DEFAULT_CLOUD_BACKEND + '/predict';
}

function updateApiIndicator() {
    const indicator = document.getElementById('apiIndicatorText');
    if (indicator) {
        const custom = localStorage.getItem('animal_backend_url');
        if (custom) {
            try {
                const url = new URL(custom);
                indicator.textContent = `Backend: ${url.host}`;
            } catch (e) {
                indicator.textContent = `Backend: ${custom}`;
            }
        } else if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
            indicator.textContent = 'Backend: localhost:8000';
        } else {
            try {
                const url = new URL(DEFAULT_CLOUD_BACKEND);
                indicator.textContent = `Backend: ${url.host}`;
            } catch (e) {
                indicator.textContent = `Backend: ${DEFAULT_CLOUD_BACKEND}`;
            }
        }
    }
}

const apiConfigBtn = document.getElementById('apiConfigBtn');
if (apiConfigBtn) {
    apiConfigBtn.addEventListener('click', () => {
        const current = localStorage.getItem('animal_backend_url') || 'http://localhost:8000';
        const newUrl = prompt(
            "Configure FastAPI Backend URL:\n\n• If running locally: http://localhost:8000\n• If using ngrok/tunnel or cloud (Render/HuggingFace): https://your-backend-url",
            current
        );
        if (newUrl !== null && newUrl.trim() !== '') {
            localStorage.setItem('animal_backend_url', newUrl.trim());
            updateApiIndicator();
            alert(`Backend URL set to: ${newUrl.trim()}`);
        }
    });
}
updateApiIndicator();

async function uploadAndPredict(file) {
    stopSpeaking();
    loadingStatus.classList.remove('hidden');
    resultsCard.classList.add('hidden');
    statusMessage.textContent = "Analyzing image features with EfficientNetB3...";

    const formData = new FormData();
    formData.append('file', file);
    const endpoint = getApiEndpoint();

    const headers = {};
    if (endpoint.includes('loca.lt')) {
        headers['bypass-tunnel-reminder'] = 'true';
    }

    try {
        const response = await fetch(endpoint, {
            method: 'POST',
            body: formData,
            headers: headers
        });

        if (!response.ok) {
            throw new Error(`Server returned error status ${response.status}`);
        }

        const data = await response.json();
        loadingStatus.classList.add('hidden');
        renderResults(data);
    } catch (err) {
        loadingStatus.classList.remove('hidden');
        if (window.location.protocol === 'https:' && (endpoint.startsWith('http://localhost') || endpoint.startsWith('http://127.0.0.1'))) {
            statusMessage.innerHTML = `⚠️ <b>Browser Mixed-Content Block:</b><br><br>` +
                `This site is loaded over secure <b>HTTPS</b>, so browsers strictly block direct calls to insecure <b>HTTP (localhost)</b>.<br><br>` +
                `👉 <b>Option 1 (Instant & Recommended):</b> Open <a href="http://localhost:8000" style="color:#60a5fa; text-decoration:underline; font-weight:bold;">http://localhost:8000</a> in your browser tab. The full web app runs locally on the same origin with zero errors.<br><br>` +
                `👉 <b>Option 2:</b> Click the <b>⚙️ Backend</b> button in the top right and enter your secure HTTPS tunnel URL.`;
        } else if (err.name === 'TypeError' && err.message.toLowerCase().includes('fetch')) {
            statusMessage.innerHTML = `⚠️ Cannot reach backend at <b>${endpoint}</b>.<br><br>• Make sure <code>python server.py</code> is running on your machine.<br>• Or click the <b>⚙️ Backend</b> button in the top right to configure your URL.`;
        } else {
            statusMessage.textContent = `❌ Error: ${err.message}`;
        }
        console.error(err);
    }
}

function renderResults(data) {
    resultsCard.classList.remove('hidden');

    const animal = data.predicted_animal;
    const emoji = ANIMAL_EMOJIS[animal] || "🐾";
    const info = data.info || {};

    animalName.textContent = animal.charAt(0).toUpperCase() + animal.slice(1);
    animalEmoji.textContent = emoji;
    confScore.textContent = `${data.confidence.toFixed(2)}%`;
    tierMessage.textContent = data.tier_message;

    // Tier badge color
    tierBadge.textContent = data.tier;
    tierBadge.className = "tier-badge";
    if (data.confidence >= 80) {
        tierBadge.classList.add('tier-high');
    } else if (data.confidence >= 50) {
        tierBadge.classList.add('tier-med');
    } else {
        tierBadge.classList.add('tier-low');
    }

    // Top 5 predictions list
    top5List.innerHTML = '';
    (data.top_5 || []).forEach(item => {
        const itemEmoji = ANIMAL_EMOJIS[item.animal] || "🐾";
        const div = document.createElement('div');
        div.className = 'top5-item';
        div.innerHTML = `
            <div class="top5-meta">
                <span>${item.rank}. ${itemEmoji} ${item.animal.charAt(0).toUpperCase() + item.animal.slice(1)}</span>
                <span>${item.confidence.toFixed(2)}%</span>
            </div>
            <div class="progress-track">
                <div class="progress-bar" style="width: ${Math.min(100, item.confidence)}%"></div>
            </div>
        `;
        top5List.appendChild(div);
    });

    // Profile & Facts
    animalOverview.textContent = info.summary || "No description available.";
    specSciName.textContent = info.scientific_name || "N/A";
    specDiet.textContent = info.diet || "N/A";
    specHabitat.textContent = info.habitat || "N/A";
    specStatus.textContent = info.status || "N/A";
    specLifespan.textContent = info.lifespan || "N/A";
    funFactText.textContent = info.fun_fact || "No fun fact recorded.";

    // Speech text setup
    currentSpeechText = info.speech || `This animal is a ${animal}.`;

    // Auto-Speak if enabled
    if (autoSpeakToggle.checked) {
        setTimeout(startSpeaking, 400);
    }
}

// Speech Synthesis
speakBtn.addEventListener('click', () => {
    startSpeaking();
});

stopBtn.addEventListener('click', () => {
    stopSpeaking();
});

function startSpeaking() {
    if (!('speechSynthesis' in window)) {
        alert("Your browser does not support the Web Speech API.");
        return;
    }

    if (!currentSpeechText) return;

    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(currentSpeechText);
    utterance.rate = 1.0;
    utterance.pitch = 1.0;

    const voices = window.speechSynthesis.getVoices();
    const englishVoice = voices.find(v => v.lang.startsWith("en") && (v.name.includes("Natural") || v.name.includes("Google") || v.name.includes("Zira") || v.name.includes("Samantha")));
    if (englishVoice) {
        utterance.voice = englishVoice;
    }

    utterance.onstart = () => {
        soundWave.classList.remove('hidden');
        voiceStatus.innerHTML = '<span class="status-dot" style="background:#38bdf8;"></span> Speaking...';
    };

    utterance.onend = () => {
        soundWave.classList.add('hidden');
        voiceStatus.innerHTML = '<span class="status-dot"></span> Finished Speaking';
    };

    utterance.onerror = () => {
        soundWave.classList.add('hidden');
        voiceStatus.innerHTML = '<span class="status-dot" style="background:#ef4444;"></span> Speech Paused';
    };

    window.speechSynthesis.speak(utterance);
}

function stopSpeaking() {
    if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
    }
    soundWave.classList.add('hidden');
    voiceStatus.innerHTML = '<span class="status-dot"></span> Ready to Speak';
}

// Pre-load voices on browser start
if ('speechSynthesis' in window) {
    window.speechSynthesis.onvoiceschanged = () => {
        window.speechSynthesis.getVoices();
    };
}
