# 📱 Mobile Access & 24/7 Always-On Server Guide

This guide explains how to access the Animal Vision & Speech AI from your mobile phone and how to keep the server running 24/7 permanently.

---

## 🚀 Part 1: Mobile Phone Access (Ready Right Now)

Your Vercel deployment has been updated with pre-configured mobile support:

### Steps to Use on Your Phone:
1. Open your mobile browser (Chrome, Safari, etc.) and go to:
   ```text
   https://animal-kohl-ten.vercel.app/
   ```
2. The website is pre-configured to use the active secure HTTPS tunnel:
   ```text
   https://animal-vision-vimal.loca.lt
   ```
3. Tap on the **📸 Take Photo or Upload Animal Image** box.
4. Your phone will prompt you to:
   - **Take Photo** using your phone's camera directly, or
   - **Choose from Photo Library / Gallery**.
5. Once selected, the model analyzes the image, displays Top-5 probabilities, and speaks educational facts aloud through your phone's speaker!

> **Note**: For local Wi-Fi testing (both phone and laptop connected to the same router):
> You can also directly open `http://10.123.184.15:8000` in your phone's browser!

---

## 🌐 Part 2: How to Keep the Server Running 24/7 ("Always Run")

If you want the backend to stay online even when your computer is shut down, you can host the backend on a free 24/7 cloud platform.

### Option A: Hugging Face Spaces (Best for ML & 100% Free Forever)
Hugging Face gives **16 GB RAM and 2 vCPUs completely free** with no credit card required. It is designed for Machine Learning models and runs 24/7.

1. Create a free account at [huggingface.co](https://huggingface.co).
2. Go to **Spaces** -> Click **Create new Space**.
3. Fill in:
   - **Space name**: `animal-vision-api`
   - **License**: `mit`
   - **Space SDK**: Select **Docker** (Blank).
   - **Visibility**: Public.
4. Click **Create Space**.
5. Connect your GitHub repository (`vimalrajifet/animal`) or push your files:
   - The included `Dockerfile` and `requirements.txt` will build automatically.
6. Once deployed, Hugging Face provides your permanent HTTPS URL:
   ```text
   https://<your-username>-animal-vision-api.hf.space
   ```
7. Click the **⚙️ Backend** button on `https://animal-kohl-ten.vercel.app/`, paste your Hugging Face URL, and your mobile app will work 24/7 forever!

---

### Option B: Render.com (Free Web Service)
1. Sign up for free at [render.com](https://render.com).
2. Click **New +** -> **Web Service**.
3. Connect your GitHub repository: `https://github.com/vimalrajifet/animal`.
4. Choose **Docker** as the runtime.
5. Choose the **Free** instance type.
6. Click **Deploy Web Service**.
7. Render gives you an HTTPS URL:
   ```text
   https://animal-backend-xxxx.onrender.com
   ```
8. Save this URL in the **⚙️ Backend** button of your website.

---

### Option C: Keep Running Locally on Windows
If you want your laptop/PC to act as your personal server:
1. Run:
   ```bash
   python server.py
   ```
2. In a second terminal, run:
   ```bash
   npx localtunnel --port 8000 --subdomain animal-vision-vimal
   ```
Your machine will continue serving requests securely to your phone as long as it is turned on.
