import React, { useState, useRef } from 'react';

/**
 * AnimalClassifier Component
 * Connects to FastAPI Backend at http://localhost:8000/predict
 * Provides image upload, prediction display, and browser text-to-speech.
 */
export default function AnimalClassifier({ apiBaseUrl = "http://localhost:8000" }) {
  const [selectedFile, setSelectedFile] = useState(null);
  const [previewUrl, setPreviewUrl] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const [isSpeaking, setIsSpeaking] = useState(false);
  const [autoSpeak, setAutoSpeak] = useState(true);
  const fileInputRef = useRef(null);

  const handleFileChange = (e) => {
    const file = e.target.files?.[0];
    if (file) processFile(file);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    const file = e.dataTransfer.files?.[0];
    if (file) processFile(file);
  };

  const processFile = (file) => {
    if (!file.type.startsWith('image/')) {
      setError("Please upload an image file (JPG, PNG, WEBP).");
      return;
    }
    setError(null);
    stopSpeaking();
    setSelectedFile(file);
    setPreviewUrl(URL.createObjectURL(file));
    uploadAndClassify(file);
  };

  const uploadAndClassify = async (file) => {
    setLoading(true);
    setResult(null);

    const formData = new FormData();
    formData.append('file', file);

    try {
      const res = await fetch(`${apiBaseUrl}/predict`, {
        method: 'POST',
        body: formData,
      });

      if (!res.ok) {
        throw new Error(`Server returned status: ${res.status}`);
      }

      const data = await res.json();
      setResult(data);

      if (autoSpeak && data.info?.speech) {
        speakText(data.info.speech);
      }
    } catch (err) {
      setError(err.message || "Failed to classify image.");
    } finally {
      setLoading(false);
    }
  };

  const speakText = (text) => {
    if (!('speechSynthesis' in window)) return;
    window.speechSynthesis.cancel();

    const utterance = new SpeechSynthesisUtterance(text);
    utterance.rate = 1.0;
    utterance.pitch = 1.0;

    const voices = window.speechSynthesis.getVoices();
    const englishVoice = voices.find(v => v.lang.startsWith("en") && (v.name.includes("Natural") || v.name.includes("Google") || v.name.includes("Zira")));
    if (englishVoice) utterance.voice = englishVoice;

    utterance.onstart = () => setIsSpeaking(true);
    utterance.onend = () => setIsSpeaking(false);
    utterance.onerror = () => setIsSpeaking(false);

    window.speechSynthesis.speak(utterance);
  };

  const stopSpeaking = () => {
    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
      setIsSpeaking(false);
    }
  };

  const reset = () => {
    stopSpeaking();
    setSelectedFile(null);
    setPreviewUrl(null);
    setResult(null);
    setError(null);
    if (fileInputRef.current) fileInputRef.current.value = "";
  };

  return (
    <div style={styles.container}>
      <header style={styles.header}>
        <div style={styles.titleGroup}>
          <span style={styles.logoIcon}>🐾</span>
          <div>
            <h1 style={styles.title}>Animal Vision AI</h1>
            <p style={styles.subtitle}>Upload an image to detect the animal and hear facts</p>
          </div>
        </div>
        <label style={styles.toggleLabel}>
          <input
            type="checkbox"
            checked={autoSpeak}
            onChange={(e) => setAutoSpeak(e.target.checked)}
          />
          Auto-Speak Facts 🗣️
        </label>
      </header>

      <div style={styles.grid}>
        {/* Upload Card */}
        <div style={styles.card}>
          <h2 style={styles.cardTitle}>Upload Animal Photo</h2>
          
          <div
            style={styles.dropZone}
            onDragOver={(e) => e.preventDefault()}
            onDrop={handleDrop}
            onClick={() => fileInputRef.current?.click()}
          >
            <input
              ref={fileInputRef}
              type="file"
              accept="image/*"
              style={{ display: 'none' }}
              onChange={handleFileChange}
            />
            {previewUrl ? (
              <div style={styles.previewContainer}>
                <img src={previewUrl} alt="Animal Preview" style={styles.previewImage} />
                <button
                  type="button"
                  style={styles.changeBtn}
                  onClick={(e) => {
                    e.stopPropagation();
                    reset();
                  }}
                >
                  ✕ Change Image
                </button>
              </div>
            ) : (
              <div>
                <div style={{ fontSize: '3rem', marginBottom: '0.8rem' }}>📁</div>
                <p style={{ fontWeight: 600, color: '#e2e8f0', marginBottom: '0.3rem' }}>
                  Click to browse or drag & drop image
                </p>
                <p style={{ fontSize: '0.85rem', color: '#94a3b8' }}>Supports JPG, PNG, WEBP</p>
              </div>
            )}
          </div>

          {loading && (
            <div style={styles.loadingBox}>
              <div style={styles.spinner}></div>
              <span>Analyzing image features with EfficientNetB3...</span>
            </div>
          )}

          {error && <div style={styles.errorBox}>❌ {error}</div>}
        </div>

        {/* Results Card */}
        {result && (
          <div style={styles.card}>
            {/* Main Result Card as specified in diagram */}
            <div style={styles.resultBox}>
              <div style={styles.resultHeader}>
                <span style={styles.tierBadge(result.confidence_level)}>
                  {result.confidence_level || result.tier}
                </span>
                <span style={styles.confidenceNumber}>{result.confidence_formatted || `${result.confidence}%`}</span>
              </div>
              <h2 style={styles.animalName}>Animal: {result.animal}</h2>
              <p style={{ color: '#cbd5e1', fontSize: '0.95rem', marginBottom: '1rem' }}>
                {result.tier_message}
              </p>

              {/* Voice Player */}
              <div style={styles.voiceBar}>
                <button
                  style={styles.speakBtn}
                  onClick={() => speakText(result.info?.speech || `This animal is a ${result.animal}`)}
                >
                  🔊 {isSpeaking ? "Speaking..." : "Say About This Animal"}
                </button>
                {isSpeaking && (
                  <button style={styles.stopBtn} onClick={stopSpeaking}>
                    ⏹️ Stop
                  </button>
                )}
              </div>
            </div>

            {/* Top 5 Predictions */}
            <h3 style={{ fontSize: '1.1rem', margin: '1.5rem 0 0.8rem 0' }}>📊 Top 5 Predictions</h3>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
              {result.top_5?.map((item, idx) => (
                <div key={idx}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.9rem', marginBottom: '3px' }}>
                    <span>{item.rank}. {item.animal}</span>
                    <span style={{ fontWeight: 600 }}>{item.confidence}%</span>
                  </div>
                  <div style={styles.progressTrack}>
                    <div style={{ ...styles.progressBar, width: `${Math.min(100, item.confidence)}%` }}></div>
                  </div>
                </div>
              ))}
            </div>

            {/* Species Encyclopedia */}
            {result.info && (
              <div style={styles.factsSection}>
                <h3 style={{ fontSize: '1.1rem', marginBottom: '0.6rem' }}>📖 About the {result.animal}</h3>
                <p style={{ fontSize: '0.95rem', lineHeight: 1.5, color: '#cbd5e1', marginBottom: '1rem' }}>
                  {result.info.summary}
                </p>

                <div style={styles.profileGrid}>
                  <div><b>🔬 Scientific:</b> {result.info.scientific_name}</div>
                  <div><b>🥩 Diet:</b> {result.info.diet}</div>
                  <div><b>🌍 Habitat:</b> {result.info.habitat}</div>
                  <div><b>🛡️ Status:</b> {result.info.status}</div>
                  <div><b>⏳ Lifespan:</b> {result.info.lifespan}</div>
                </div>

                {result.info.fun_fact && (
                  <div style={styles.funFactCard}>
                    💡 <b>Fascinating Fact:</b><br />
                    {result.info.fun_fact}
                  </div>
                )}
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

const styles = {
  container: {
    maxWidth: '1200px',
    margin: '0 auto',
    padding: '2rem 1.5rem',
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
    color: '#f8fafc',
  },
  header: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: '2rem',
    paddingBottom: '1rem',
    borderBottom: '1px solid rgba(255, 255, 255, 0.1)',
  },
  titleGroup: {
    display: 'flex',
    alignItems: 'center',
    gap: '12px',
  },
  logoIcon: { fontSize: '2.5rem' },
  title: {
    fontSize: '1.8rem',
    fontWeight: 800,
    background: 'linear-gradient(135deg, #3b82f6, #8b5cf6, #ec4899)',
    WebkitBackgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
    margin: 0,
  },
  subtitle: { color: '#94a3b8', fontSize: '0.9rem', margin: 0 },
  toggleLabel: {
    display: 'flex',
    alignItems: 'center',
    gap: '8px',
    fontSize: '0.9rem',
    cursor: 'pointer',
    background: 'rgba(255, 255, 255, 0.05)',
    padding: '8px 14px',
    borderRadius: '9999px',
  },
  grid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(360px, 1fr))',
    gap: '2rem',
  },
  card: {
    background: 'rgba(18, 24, 38, 0.85)',
    border: '1px solid rgba(255, 255, 255, 0.08)',
    borderRadius: '20px',
    padding: '1.8rem',
    boxShadow: '0 8px 32px rgba(0,0,0,0.3)',
  },
  cardTitle: { fontSize: '1.3rem', fontWeight: 700, marginBottom: '1.2rem' },
  dropZone: {
    border: '2px dashed rgba(99, 102, 241, 0.4)',
    borderRadius: '16px',
    padding: '2.5rem 1.5rem',
    textAlign: 'center',
    background: 'rgba(15, 23, 42, 0.5)',
    cursor: 'pointer',
    minHeight: '240px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  },
  previewContainer: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    gap: '12px',
    width: '100%',
  },
  previewImage: {
    maxWidth: '100%',
    maxHeight: '260px',
    borderRadius: '12px',
    objectFit: 'contain',
  },
  changeBtn: {
    background: 'rgba(239, 68, 68, 0.2)',
    color: '#f87171',
    border: '1px solid rgba(239, 68, 68, 0.4)',
    padding: '6px 14px',
    borderRadius: '8px',
    cursor: 'pointer',
    fontWeight: 600,
  },
  loadingBox: {
    display: 'flex',
    alignItems: 'center',
    gap: '12px',
    marginTop: '1.2rem',
    padding: '12px',
    background: 'rgba(59, 130, 246, 0.1)',
    borderRadius: '10px',
    color: '#93c5fd',
  },
  spinner: {
    width: '18px',
    height: '18px',
    border: '2px solid rgba(147, 197, 253, 0.3)',
    borderTopColor: '#60a5fa',
    borderRadius: '50%',
  },
  errorBox: {
    marginTop: '1.2rem',
    padding: '12px',
    background: 'rgba(239, 68, 68, 0.15)',
    border: '1px solid #ef4444',
    borderRadius: '10px',
    color: '#fca5a5',
  },
  resultBox: {
    background: 'linear-gradient(135deg, rgba(59, 130, 246, 0.12), rgba(139, 92, 246, 0.12))',
    border: '1px solid rgba(139, 92, 246, 0.3)',
    borderRadius: '16px',
    padding: '1.5rem',
  },
  resultHeader: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: '0.6rem',
  },
  tierBadge: (tier) => ({
    padding: '4px 12px',
    borderRadius: '9999px',
    fontSize: '0.8rem',
    fontWeight: 700,
    textTransform: 'uppercase',
    background: tier === 'High Confidence' ? 'rgba(34, 197, 94, 0.15)' : 'rgba(234, 179, 8, 0.15)',
    color: tier === 'High Confidence' ? '#4ade80' : '#facc15',
    border: `1px solid ${tier === 'High Confidence' ? '#22c55e' : '#eab308'}`,
  }),
  confidenceNumber: {
    fontSize: '1.6rem',
    fontWeight: 800,
    color: '#60a5fa',
  },
  animalName: {
    fontSize: '2rem',
    fontWeight: 800,
    margin: '0.4rem 0',
  },
  voiceBar: {
    display: 'flex',
    gap: '10px',
    alignItems: 'center',
    background: 'rgba(15, 23, 42, 0.8)',
    padding: '10px 14px',
    borderRadius: '12px',
  },
  speakBtn: {
    background: 'linear-gradient(135deg, #2563eb, #7c3aed)',
    color: '#fff',
    border: 'none',
    padding: '8px 16px',
    borderRadius: '8px',
    fontWeight: 600,
    cursor: 'pointer',
  },
  stopBtn: {
    background: 'rgba(239, 68, 68, 0.2)',
    color: '#f87171',
    border: '1px solid rgba(239, 68, 68, 0.4)',
    padding: '8px 12px',
    borderRadius: '8px',
    fontWeight: 600,
    cursor: 'pointer',
  },
  progressTrack: {
    background: 'rgba(255, 255, 255, 0.08)',
    height: '8px',
    borderRadius: '9999px',
    overflow: 'hidden',
  },
  progressBar: {
    height: '100%',
    borderRadius: '9999px',
    background: 'linear-gradient(90deg, #3b82f6, #8b5cf6)',
  },
  factsSection: {
    marginTop: '1.5rem',
    paddingTop: '1.2rem',
    borderTop: '1px solid rgba(255, 255, 255, 0.08)',
  },
  profileGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(160px, 1fr))',
    gap: '10px',
    fontSize: '0.85rem',
    marginBottom: '1rem',
  },
  funFactCard: {
    background: 'linear-gradient(135deg, rgba(245, 158, 11, 0.1), rgba(217, 119, 6, 0.15))',
    borderLeft: '4px solid #f59e0b',
    borderRadius: '8px',
    padding: '1rem',
    fontSize: '0.9rem',
    color: '#fef3c7',
  },
};
