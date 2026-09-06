"""
Streamlit Web Application for 90-Class Animal Classification
Connects the local archive dataset and trained EfficientNetB3 model for real-time inference,
complete with voice narration (Text-to-Speech) and encyclopedic animal facts.
"""

import os
import sys
import json
import random
import numpy as np
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components

from animal_data import get_animal_info, ANIMAL_INFO

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Page configuration
st.set_page_config(
    page_title="90-Animal Classifier & Encyclopedia",
    page_icon="🦁",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Animal Emojis mapping
ANIMAL_EMOJIS = {
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
}

# Custom Styling for modern, polished UI
st.markdown("""
<style>
    .main-header {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #2563eb, #7c3aed, #db2777);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        color: #64748b;
        font-size: 1.05rem;
        margin-bottom: 1.5rem;
    }
    .prediction-card {
        background: linear-gradient(135deg, rgba(37, 99, 235, 0.08), rgba(124, 58, 237, 0.08));
        border: 1px solid rgba(124, 58, 237, 0.25);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1.2rem;
    }
    .animal-title {
        font-size: 2.2rem;
        font-weight: 800;
        margin-bottom: 0.2rem;
    }
    .tier-badge {
        display: inline-block;
        padding: 0.35rem 0.85rem;
        border-radius: 9999px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 0.8rem;
    }
    .tier-high {
        background-color: #dcfce7;
        color: #15803d;
        border: 1px solid #86efac;
    }
    .tier-med {
        background-color: #fef9c3;
        color: #a16207;
        border: 1px solid #fde047;
    }
    .tier-low {
        background-color: #fee2e2;
        color: #b91c1c;
        border: 1px solid #fca5a5;
    }
    .facts-card {
        background: rgba(255, 255, 255, 0.65);
        backdrop-filter: blur(10px);
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 1.5rem;
        margin-top: 1.2rem;
    }
    .fact-item {
        margin-bottom: 0.75rem;
        font-size: 0.95rem;
    }
    .fact-label {
        font-weight: 700;
        color: #3b82f6;
    }
    .fun-fact-box {
        background: linear-gradient(135deg, #fef3c7, #fde68a);
        border-left: 5px solid #d97706;
        border-radius: 8px;
        padding: 1rem;
        color: #78350f;
        font-weight: 500;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)


def render_voice_narrator(speech_text, auto_play=False):
    """
    Renders an HTML5 / Web Speech API voice synthesis component.
    Plays speech directly in the client browser with no external audio server required.
    """
    escaped_text = json.dumps(speech_text)
    auto_play_js = "true" if auto_play else "false"

    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        body {{
            margin: 0;
            padding: 10px 0;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: transparent;
        }}
        .audio-bar {{
            display: flex;
            align-items: center;
            gap: 12px;
            background: linear-gradient(135deg, #1e293b, #0f172a);
            padding: 12px 18px;
            border-radius: 12px;
            color: white;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }}
        .btn {{
            border: none;
            border-radius: 8px;
            padding: 9px 18px;
            font-weight: 600;
            font-size: 0.95rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 6px;
            transition: all 0.2s ease;
        }}
        .btn-speak {{
            background: linear-gradient(135deg, #3b82f6, #8b5cf6);
            color: white;
        }}
        .btn-speak:hover {{
            transform: scale(1.03);
            box-shadow: 0 4px 14px rgba(99, 102, 241, 0.4);
        }}
        .btn-stop {{
            background: rgba(239, 68, 68, 0.2);
            color: #f87171;
            border: 1px solid rgba(239, 68, 68, 0.4);
        }}
        .btn-stop:hover {{
            background: rgba(239, 68, 68, 0.4);
        }}
        .status {{
            font-size: 0.85rem;
            color: #94a3b8;
            margin-left: auto;
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        .dot {{
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: #22c55e;
            display: inline-block;
        }}
        .speaking-anim {{
            display: none;
            gap: 3px;
            align-items: center;
            height: 16px;
        }}
        .bar {{
            width: 3px;
            background: #38bdf8;
            border-radius: 2px;
            animation: bounce 0.6s infinite alternate ease-in-out;
        }}
        .bar:nth-child(2) {{ animation-delay: 0.2s; height: 14px; }}
        .bar:nth-child(3) {{ animation-delay: 0.4s; height: 18px; }}
        .bar:nth-child(4) {{ animation-delay: 0.1s; height: 10px; }}
        @keyframes bounce {{
            from {{ height: 4px; }}
            to {{ height: 18px; }}
        }}
    </style>
    </head>
    <body>
        <div class="audio-bar">
            <button class="btn btn-speak" id="playBtn" onclick="speakText()">
                🔊 Say About This Animal
            </button>
            <button class="btn btn-stop" id="stopBtn" onclick="stopSpeech()">
                ⏹️ Stop
            </button>
            <div class="speaking-anim" id="soundWaves">
                <div class="bar"></div>
                <div class="bar"></div>
                <div class="bar"></div>
                <div class="bar"></div>
            </div>
            <div class="status" id="statusText">
                <span class="dot"></span> Voice Ready
            </div>
        </div>

        <script>
            const textToSpeak = {escaped_text};
            const autoPlay = {auto_play_js};

            function speakText() {{
                if (!('speechSynthesis' in window)) {{
                    alert("Your browser does not support Speech Synthesis.");
                    return;
                }}

                window.speechSynthesis.cancel();
                const utterance = new SpeechSynthesisUtterance(textToSpeak);
                utterance.rate = 1.0;
                utterance.pitch = 1.0;

                // Pick a smooth natural voice if available
                const voices = window.speechSynthesis.getVoices();
                const englishVoice = voices.find(v => v.lang.startsWith("en") && (v.name.includes("Natural") || v.name.includes("Google") || v.name.includes("Zira") || v.name.includes("Samantha")));
                if (englishVoice) {{
                    utterance.voice = englishVoice;
                }}

                utterance.onstart = function() {{
                    document.getElementById('soundWaves').style.display = 'flex';
                    document.getElementById('statusText').innerHTML = '<span class="dot" style="background:#38bdf8;"></span> Speaking...';
                }};

                utterance.onend = function() {{
                    document.getElementById('soundWaves').style.display = 'none';
                    document.getElementById('statusText').innerHTML = '<span class="dot"></span> Finished speaking';
                }};

                utterance.onerror = function() {{
                    document.getElementById('soundWaves').style.display = 'none';
                    document.getElementById('statusText').innerHTML = '<span class="dot" style="background:#ef4444;"></span> Speech paused';
                }};

                window.speechSynthesis.speak(utterance);
            }}

            function stopSpeech() {{
                window.speechSynthesis.cancel();
                document.getElementById('soundWaves').style.display = 'none';
                document.getElementById('statusText').innerHTML = '<span class="dot"></span> Stopped';
            }}

            // Run automatically if requested
            if (autoPlay) {{
                window.addEventListener('load', function() {{
                    setTimeout(speakText, 400);
                }});
            }}
        </script>
    </body>
    </html>
    """
    components.html(html_code, height=75)


@st.cache_resource
def load_class_names():
    classes_path = os.path.join(os.path.dirname(__file__), "classes.json")
    if os.path.exists(classes_path):
        with open(classes_path, "r", encoding="utf-8") as f:
            return json.load(f)
    
    txt_path = os.path.join(os.path.dirname(__file__), "archive", "name of the animals.txt")
    if os.path.exists(txt_path):
        with open(txt_path, "r", encoding="utf-8") as f:
            return [l.strip() for l in f if l.strip()]
    return []


@st.cache_resource
def load_model(model_path="best_animal_model.keras"):
    if not os.path.exists(model_path):
        return None
    import tensorflow as tf
    try:
        model = tf.keras.models.load_model(model_path)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None


def run_prediction(model, image, classes, img_size=300):
    resized = image.resize((img_size, img_size))
    img_array = np.array(resized, dtype=np.float32)
    img_batch = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_batch, verbose=0)[0]
    best_idx = int(np.argmax(predictions))
    best_animal = classes[best_idx]
    best_conf = float(predictions[best_idx] * 100)

    top_5_indices = np.argsort(predictions)[-5:][::-1]
    top_5 = [
        {
            "rank": r,
            "animal": classes[idx],
            "confidence": float(predictions[idx] * 100),
            "emoji": ANIMAL_EMOJIS.get(classes[idx], "🐾")
        }
        for r, idx in enumerate(top_5_indices, 1)
    ]

    return best_animal, best_conf, top_5


def main():
    st.markdown('<div class="main-header">🐾 90-Animal Classifier & Encyclopedia</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Upload an animal photo to detect the species, hear live voice narration, and discover complete wildlife facts.</div>', unsafe_allow_html=True)

    classes = load_class_names()
    model_path = os.path.join(os.path.dirname(__file__), "best_animal_model.keras")
    model = load_model(model_path)

    # Sidebar controls
    with st.sidebar:
        st.header("⚙️ Settings & Audio")
        auto_narrate = st.checkbox("🗣️ Auto-Speak on Prediction", value=False, help="Automatically read animal facts aloud whenever a new image is loaded.")

        st.markdown("---")
        st.header("📊 Model & Dataset")
        if model is not None:
            st.success("✅ Model Loaded (`best_animal_model.keras`)")
        else:
            st.warning("⚠️ Model not found (`best_animal_model.keras`).")

        st.metric("Total Animal Classes", len(classes))
        st.markdown("**Backbone Architecture:** EfficientNetB3")
        st.markdown("**Dataset Path:** `archive/animals/animals`")

        st.markdown("---")
        st.subheader("💡 What This App Does")
        st.markdown(
            "1. **Classifies** your photo into one of 90 animal species.<br>"
            "2. **Speaks aloud** about the animal using browser speech synthesis.<br>"
            "3. **Displays** scientific name, diet, habitat, and fun trivia.",
            unsafe_allow_html=True
        )

    # Main interaction mode
    tab1, tab2 = st.tabs(["📁 Upload Your Own Image", "🦁 Test from Dataset Gallery"])

    selected_image = None
    source_info = ""

    with tab1:
        uploaded_file = st.file_uploader(
            "Choose an animal photo (JPG, JPEG, PNG, WEBP)",
            type=["jpg", "jpeg", "png", "webp"]
        )
        if uploaded_file is not None:
            selected_image = Image.open(uploaded_file).convert("RGB")
            source_info = f"Uploaded File: `{uploaded_file.name}`"

    with tab2:
        st.markdown("Test an image straight from the **90-class archive dataset** on your drive:")
        archive_root = os.path.join(os.path.dirname(__file__), "archive", "animals", "animals")
        
        if os.path.exists(archive_root):
            col_sel1, col_sel2 = st.columns([3, 1])
            with col_sel1:
                chosen_class = st.selectbox("Select an animal category:", classes, index=classes.index("tiger") if "tiger" in classes else 0)
            with col_sel2:
                random_btn = st.button("🎲 Random Animal", use_container_width=True)
                if random_btn:
                    chosen_class = random.choice(classes)

            class_dir = os.path.join(archive_root, chosen_class)
            if os.path.exists(class_dir):
                sample_files = [f for f in os.listdir(class_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
                if sample_files:
                    cols = st.columns(min(4, len(sample_files)))
                    for i, fname in enumerate(sample_files[:4]):
                        img_p = os.path.join(class_dir, fname)
                        with cols[i]:
                            thumb = Image.open(img_p).convert("RGB")
                            emoji = ANIMAL_EMOJIS.get(chosen_class, "🐾")
                            st.image(thumb, use_container_width=True, caption=f"{emoji} {chosen_class.title()} #{i+1}")
                            if st.button(f"Test #{i+1}", key=f"btn_{chosen_class}_{i}"):
                                selected_image = thumb
                                source_info = f"Archive Sample: `{chosen_class}` / `{fname}`"
        else:
            st.warning("Archive folder not found at `archive/animals/animals`.")

    # Results section
    if selected_image is not None:
        st.markdown("---")
        col_img, col_res = st.columns([1, 1], gap="large")

        with col_img:
            st.subheader("📷 Image Preview")
            st.image(selected_image, use_container_width=True)
            st.caption(f"{source_info} | Dimensions: {selected_image.size[0]}×{selected_image.size[1]} px")

        with col_res:
            st.subheader("🎯 Prediction Results")
            if model is None:
                st.error("No trained model found. Please train the model using `python train.py` first.")
            else:
                with st.spinner("Analyzing image features with EfficientNetB3..."):
                    best_animal, best_conf, top_5 = run_prediction(model, selected_image, classes)

                emoji = ANIMAL_EMOJIS.get(best_animal, "🐾")
                animal_info = get_animal_info(best_animal)

                # Tier badge logic
                if best_conf >= 80:
                    tier_class = "tier-high"
                    tier_text = "✅ High Confidence"
                    tier_desc = f"This animal is most likely a <b>{best_animal.title()}</b>."
                elif best_conf >= 50:
                    tier_class = "tier-med"
                    tier_text = "⚠️ Medium Confidence"
                    tier_desc = f"The animal may be a <b>{best_animal.title()}</b>."
                else:
                    tier_class = "tier-low"
                    tier_text = "❓ Low Confidence"
                    tier_desc = f"Low confidence prediction. Best guess: <b>{best_animal.title()}</b>."

                # Prediction Card
                st.markdown(f"""
                <div class="prediction-card">
                    <div class="tier-badge {tier_class}">{tier_text}</div>
                    <div class="animal-title">{emoji} {best_animal.title()}</div>
                    <div style="font-size: 1.6rem; font-weight: 800; color: #2563eb; margin-bottom: 0.5rem;">
                        {best_conf:.2f}% Confidence
                    </div>
                    <div style="font-size: 0.95rem;">
                        {tier_desc}
                    </div>
                </div>
                """, unsafe_allow_html=True)

                st.subheader("📊 Top 5 Predictions")
                for item in top_5:
                    c1, c2 = st.columns([3, 1])
                    with c1:
                        st.markdown(f"**{item['rank']}. {item['emoji']} {item['animal'].title()}**")
                        st.progress(float(min(1.0, item["confidence"] / 100)))
                    with c2:
                        st.markdown(f"<div style='text-align: right; padding-top: 5px; font-weight: 700;'>{item['confidence']:.2f}%</div>", unsafe_allow_html=True)

        # 📖 Full Animal Knowledge & Voice Narration Section
        if model is not None and 'best_animal' in locals():
            st.markdown("---")
            st.subheader(f"📖 About the {best_animal.title()}")

            # Voice Narrator Audio Component
            render_voice_narrator(animal_info["speech"], auto_play=auto_narrate)

            # Facts Cards
            c_info1, c_info2 = st.columns([3, 2], gap="large")

            with c_info1:
                st.markdown(f"**Overview:**")
                st.write(animal_info["summary"])

                st.markdown(f"""
                <div class="fun-fact-box">
                    💡 <b>Fascinating Fact:</b><br>{animal_info["fun_fact"]}
                </div>
                """, unsafe_allow_html=True)

            with c_info2:
                st.markdown("**Species Profile:**")
                st.markdown(f"- 🔬 **Scientific Name:** *{animal_info['scientific_name']}*")
                st.markdown(f"- 🥩 **Diet:** {animal_info['diet']}")
                st.markdown(f"- 🌍 **Habitat:** {animal_info['habitat']}")
                st.markdown(f"- 🛡️ **Conservation Status:** {animal_info['status']}")
                st.markdown(f"- ⏳ **Typical Lifespan:** {animal_info['lifespan']}")


if __name__ == "__main__":
    main()
