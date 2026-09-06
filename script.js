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

let ortSession = null;
let classesCache = null;
let animalInfoCache = null;

async function loadStaticData() {
    if (!classesCache) {
        try {
            const res = await fetch('classes.json');
            classesCache = await res.json();
        } catch (e) {
            console.warn("Could not load classes.json", e);
        }
    }
    if (!animalInfoCache) {
        try {
            const res = await fetch('animal_data.json');
            animalInfoCache = await res.json();
        } catch (e) {
            console.warn("Could not load animal_data.json", e);
        }
    }
}
loadStaticData();

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
        } else {
            indicator.textContent = '🧠 AI: In-Browser (Free & Offline)';
        }
    }
}

const apiConfigBtn = document.getElementById('apiConfigBtn');
if (apiConfigBtn) {
    apiConfigBtn.addEventListener('click', () => {
        const current = localStorage.getItem('animal_backend_url') || '';
        const newUrl = prompt(
            "Configure Backend (Optional):\n\n• Leave blank to use 100% Free In-Browser AI (recommended)\n• Or paste your custom cloud URL (e.g. https://animal-api.onrender.com):",
            current
        );
        if (newUrl !== null) {
            if (newUrl.trim() === '') {
                localStorage.removeItem('animal_backend_url');
                alert("Switched to 100% Free In-Browser AI engine!");
            } else {
                localStorage.setItem('animal_backend_url', newUrl.trim());
                alert(`Backend set to: ${newUrl.trim()}`);
            }
            updateApiIndicator();
        }
    });
}
updateApiIndicator();

async function getOrInitOrtSession() {
    if (ortSession) return ortSession;
    statusMessage.textContent = "Loading AI vision engine in your browser (first time only ~41MB)...";
    if (typeof ort !== 'undefined') {
        ort.env.wasm.numThreads = 1;
        ort.env.wasm.simd = true;
        ortSession = await ort.InferenceSession.create('animal_model.onnx', {
            executionProviders: ['wasm']
        });
        return ortSession;
    }
    throw new Error("ONNX Runtime Web library could not be loaded.");
}

async function predictInBrowser(file) {
    statusMessage.textContent = "Preparing image...";
    await loadStaticData();

    const img = new Image();
    const url = URL.createObjectURL(file);
    await new Promise((resolve, reject) => {
        img.onload = () => resolve();
        img.onerror = reject;
        img.src = url;
    });

    const session = await getOrInitOrtSession();
    statusMessage.textContent = "Analyzing animal features with EfficientNetB3...";

    const canvas = document.createElement('canvas');
    canvas.width = 300;
    canvas.height = 300;
    const ctx = canvas.getContext('2d');
    ctx.drawImage(img, 0, 0, 300, 300);
    URL.revokeObjectURL(url);

    const imgData = ctx.getImageData(0, 0, 300, 300).data;
    const floatArray = new Float32Array(1 * 300 * 300 * 3);

    for (let i = 0, j = 0; i < imgData.length; i += 4, j += 3) {
        floatArray[j] = imgData[i];
        floatArray[j + 1] = imgData[i + 1];
        floatArray[j + 2] = imgData[i + 2];
    }

    const inputTensor = new ort.Tensor('float32', floatArray, [1, 300, 300, 3]);
    const outputMap = await session.run({ input: inputTensor });
    const outputTensor = outputMap.dense || Object.values(outputMap)[0];
    const probs = Array.from(outputTensor.data);

    const indexed = probs.map((val, idx) => ({ val, idx }));
    indexed.sort((a, b) => b.val - a.val);

    const best = indexed[0];
    const rawName = (classesCache && classesCache[best.idx]) || `Class ${best.idx}`;
    const bestName = rawName.charAt(0).toUpperCase() + rawName.slice(1);
    const confidencePct = Math.round(best.val * 10000) / 100;

    let tier = "Low Confidence";
    let tierMsg = `Low confidence prediction. Best guess: ${bestName}.`;
    if (confidencePct >= 80) {
        tier = "High Confidence";
        tierMsg = `Strong match! Identified as ${bestName} with high certainty.`;
    } else if (confidencePct >= 50) {
        tier = "Medium Confidence";
        tierMsg = `Moderate match. Likely a ${bestName}.`;
    }

    const top5 = indexed.slice(0, 5).map((item, r) => {
        const name = (classesCache && classesCache[item.idx]) || `Class ${item.idx}`;
        return {
            rank: r + 1,
            animal: name.charAt(0).toUpperCase() + name.slice(1),
            confidence: Math.round(item.val * 10000) / 100
        };
    });

    const key = rawName.toLowerCase();
    const info = (animalInfoCache && animalInfoCache[key]) || {
        scientific_name: bestName,
        diet: "Unknown",
        habitat: "Wild",
        status: "Least Concern",
        lifespan: "Unknown",
        summary: `${bestName} is a wonderful creature recognized by our AI vision model.`,
        fun_fact: `Animals of type ${bestName} play an essential role in their natural ecosystem.`,
        speech: `This is a ${bestName}. Our AI vision model has detected this species with a confidence score of ${confidencePct} percent.`
    };

    return {
        success: true,
        animal: bestName,
        predicted_animal: key,
        confidence: confidencePct,
        confidence_formatted: `${confidencePct}%`,
        confidence_level: tier,
        tier: tier,
        tier_message: tierMsg,
        top_5: top5,
        info: info
    };
}

async function uploadAndPredict(file) {
    stopSpeaking();
    loadingStatus.classList.remove('hidden');
    resultsCard.classList.add('hidden');
    statusMessage.textContent = "Analyzing image features with EfficientNetB3...";

    const customUrl = localStorage.getItem('animal_backend_url');
    if (customUrl) {
        const endpoint = customUrl.replace(/\/+$/, '') + '/predict';
        try {
            const formData = new FormData();
            formData.append('file', file);
            const headers = {};
            if (endpoint.includes('loca.lt')) headers['bypass-tunnel-reminder'] = 'true';

            const response = await fetch(endpoint, {
                method: 'POST',
                body: formData,
                headers: headers
            });
            if (response.ok) {
                const data = await response.json();
                loadingStatus.classList.add('hidden');
                renderResults(data);
                return;
            }
        } catch (e) {
            console.warn("Custom backend error, using in-browser AI:", e);
        }
    }

    try {
        const data = await predictInBrowser(file);
        loadingStatus.classList.add('hidden');
        renderResults(data);
    } catch (err) {
        loadingStatus.classList.remove('hidden');
        statusMessage.textContent = `❌ Prediction error: ${err.message}`;
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
